from __future__ import annotations

import asyncio
import datetime
import random
import time
from contextlib import ExitStack
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Sequence, Type

from sibi_dst.utils import ManagedResource

try:
    from dask.distributed import Client, LocalCluster
except ImportError:
    Client = None
    LocalCluster = None


@dataclass(slots=True)
class _RetryCfg:
    attempts: int = 3
    backoff_base: float = 2.0
    backoff_max: float = 60.0
    jitter: float = 0.15


# ---------------- Worker (safe for Dask pickling) ----------------
def run_artifact_update(
    cls: Type,
    artifact_class_kwargs: Dict[str, Any],
    retry: _RetryCfg,
    period: str,
    artifact_kwargs: Dict[str, Any],
) -> Dict[str, Any]:
    """Standalone worker — safe for Dask distributed execution."""
    import logging

    logger = logging.getLogger(cls.__name__)

    start_wall = datetime.datetime.now()
    attempt_count = 0
    success = False
    error_msg = None

    for attempt in range(1, retry.attempts + 1):
        attempt_count = attempt
        try:
            with ExitStack() as stack:
                inst = cls(**artifact_class_kwargs)
                inst = stack.enter_context(inst)
                inst.update_parquet(period=period, **artifact_kwargs)
            success = True
            break
        except Exception as e:
            error_msg = str(e)
            if attempt < retry.attempts:
                delay = min(retry.backoff_base ** (attempt - 1), retry.backoff_max)
                delay *= 1 + random.uniform(0, retry.jitter)
                time.sleep(delay)

    end_wall = datetime.datetime.now()
    duration = (end_wall - start_wall).total_seconds()

    return {
        "artifact": cls.__name__,
        "period": period,
        "start": start_wall.isoformat(),
        "end": end_wall.isoformat(),
        "processing_time": duration,
        "retries": attempt_count - 1 if success else attempt_count,
        "success": success,
        "error": error_msg,
    }


class ArtifactUpdaterMultiWrapperAsync(ManagedResource):
    """
    Async/Threaded orchestrator.
    Dask-enabled if a Client is passed (or created automatically).
    """

    def __init__(
        self,
        wrapped_classes: Dict[str, Sequence[Type]],
        *,
        max_workers: int = 3,
        retry_attempts: int = 3,
        update_timeout_seconds: int = 600,
        backoff_base: float = 2.0,
        backoff_max: float = 60.0,
        backoff_jitter: float = 0.15,
        priority_fn: Optional[Callable[[Type], int]] = None,
        artifact_class_kwargs: Optional[Dict[str, Any]] = None,
        dask_client: Optional[Client] = None,
        use_dask: bool = True,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)

        self.wrapped_classes = wrapped_classes
        self.max_workers = int(max_workers)
        self.update_timeout_seconds = int(update_timeout_seconds)
        self.priority_fn = priority_fn
        self.use_dask = use_dask
        self.client: Optional[Client] = dask_client
        self._owns_client = False

        self._retry = _RetryCfg(
            attempts=int(retry_attempts),
            backoff_base=float(backoff_base),
            backoff_max=float(backoff_max),
            jitter=float(backoff_jitter),
        )

        # Safe kwargs for artifacts
        if self.use_dask:
            self.artifact_class_kwargs = {
                "debug": self.debug,
                "verbose": self.verbose,
                **(artifact_class_kwargs or {}),
            }
        else:
            self.artifact_class_kwargs = {
                "logger": self.logger,
                "fs": self.fs,
                "debug": self.debug,
                "verbose": self.verbose,
                **(artifact_class_kwargs or {}),
            }

        self.completion_secs: Dict[str, float] = {}
        self.failed: List[str] = []
        self._stop = asyncio.Event()

        if self.use_dask and Client is None:
            raise RuntimeError("Dask is not installed, cannot use Dask mode")

        # auto-start local client if requested
        if self.use_dask and not self.client:
            self.client = Client(
                LocalCluster(
                    n_workers=max_workers,
                    threads_per_worker=1,
                    dashboard_address=None,
                )
            )
            self._owns_client = True

    # ---- Internals ------------------------------------------------------------

    def _classes_for(self, period: str) -> List[Type]:
        try:
            classes = list(self.wrapped_classes[period])
        except KeyError:
            raise ValueError(f"Unsupported period '{period}'.")
        if not classes:
            raise ValueError(f"No artifact classes configured for '{period}'.")
        if self.priority_fn:
            try:
                classes.sort(key=self.priority_fn)
            except Exception as e:
                self.logger.warning(f"priority_fn failed; using listed order: {e}")
        return classes

    def _submit_one_dask(self, cls: Type, period: str, artifact_kwargs: Dict[str, Any]):
        return self.client.submit(
            run_artifact_update,
            cls,
            dict(self.artifact_class_kwargs),
            self._retry,
            period,
            artifact_kwargs,
            pure=False,
        )

    async def _run_one_async(
        self,
        cls: Type,
        period: str,
        sem: asyncio.Semaphore,
        artifact_kwargs: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Async/threaded fallback execution."""
        name = cls.__name__
        self.logger.info(f"▶️ Starting {name} for period '{period}'")
        start_wall = datetime.datetime.now()

        attempt_count = 0
        success = False
        error_msg = None

        try:
            async with sem:
                for attempt in range(1, self._retry.attempts + 1):
                    attempt_count = attempt
                    try:
                        def _sync_block():
                            with ExitStack() as stack:
                                inst = cls(**self.artifact_class_kwargs)
                                inst = stack.enter_context(inst)
                                inst.update_parquet(period=period, **artifact_kwargs)

                        await asyncio.wait_for(
                            asyncio.to_thread(_sync_block),
                            timeout=self.update_timeout_seconds,
                        )
                        success = True
                        break
                    except Exception as e:
                        error_msg = str(e)
                        if attempt < self._retry.attempts and not self._stop.is_set():
                            delay = min(
                                self._retry.backoff_base ** (attempt - 1),
                                self._retry.backoff_max,
                            )
                            delay *= 1 + random.uniform(0, self._retry.jitter)
                            await asyncio.sleep(delay)
        finally:
            end_wall = datetime.datetime.now()
            duration = (end_wall - start_wall).total_seconds()

            result = {
                "artifact": name,
                "period": period,
                "start": start_wall.isoformat(),
                "end": end_wall.isoformat(),
                "processing_time": duration,
                "retries": attempt_count - 1 if success else attempt_count,
                "success": success,
                "error": error_msg,
            }

            if success:
                self.logger.info(f"✅ Artifact {name} succeeded", extra=result)
                self.completion_secs[name] = duration
            else:
                self.logger.error(f"❌ Artifact {name} failed", extra=result)
                self.failed.append(name)

            return result

    # ---- Public API -----------------------------------------------------------

    async def update_data(self, period: str, **kwargs: Any) -> List[Dict[str, Any]]:
        self.completion_secs.clear()
        self.failed.clear()
        classes = self._classes_for(period)

        try:
            if self.use_dask:
                futures = [self._submit_one_dask(cls, period, kwargs) for cls in classes]
                results = await asyncio.to_thread(lambda: self.client.gather(futures))
            else:
                sem = asyncio.Semaphore(self.max_workers)
                tasks = [
                    asyncio.create_task(self._run_one_async(cls, period, sem, kwargs))
                    for cls in classes
                ]
                results = await asyncio.gather(*tasks)
            return results
        finally:
            # only shut down if we own the client
            if self._owns_client:
                self.close()

    def get_update_status(self) -> Dict[str, Any]:
        done = set(self.completion_secs)
        fail = set(self.failed)
        all_names = {c.__name__ for v in self.wrapped_classes.values() for c in v}
        return {
            "total": len(all_names),
            "completed": sorted(done),
            "failed": sorted(fail),
            "pending": sorted(all_names - done - fail),
            "completion_times": dict(self.completion_secs),
        }

    # ---- Lifecycle ------------------------------------------------------------

    def _cleanup(self) -> None:
        """Release any resources created by this wrapper."""
        if self._owns_client and self.client is not None:
            try:
                cluster = getattr(self.client, "cluster", None)
                self.client.close()
                if cluster is not None:
                    cluster.close()
            finally:
                self.client = None
                self._owns_client = False

