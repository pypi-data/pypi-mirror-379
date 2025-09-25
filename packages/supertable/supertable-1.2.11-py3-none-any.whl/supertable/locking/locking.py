# supertable/locking/locking.py

import json
import time
import fcntl
from typing import Any, Dict, Iterable, List, Optional

from supertable.config.defaults import default
from supertable.locking.file_lock import FileLocking
from supertable.locking.locking_backend import LockingBackend


class Locking:
    """
    Facade over concrete locking backends (file or redis). Keeps the public API
    stable for callers (e.g. SuperTable) and delegates to the selected backend.

    Notes:
      - When STORAGE_TYPE == 'LOCAL' (default), file-based locking is used.
      - Otherwise, Redis-based locking is used (requires redis extras installed).
      - `lock_shared_and_read` is only meaningful on LOCAL/file backend because
        it relies on OS-level shared file locks. For non-LOCAL storage types,
        callers should rely on the storage backend’s own consistency or use the
        exclusive lock + read pattern.
    """

    def __init__(
        self,
        identity: str,
        backend: Optional[LockingBackend] = None,
        working_dir: Optional[str] = None,
        lock_file_name: str = ".lock.json",
        check_interval: float = 0.1,
        **kwargs: Any,
    ) -> None:
        self.identity = identity
        self.check_interval = float(check_interval)

        # Auto-detect backend if not explicitly provided
        if backend is None:
            storage_type = getattr(default, "STORAGE_TYPE", "LOCAL").upper()
            backend = LockingBackend.FILE if storage_type == "LOCAL" else LockingBackend.REDIS
        self.backend = backend

        # Instantiate backend
        if self.backend == LockingBackend.FILE:
            # working_dir is required for file-based locking
            self.lock_instance = FileLocking(
                identity=identity,
                working_dir=working_dir,
                lock_file_name=lock_file_name,
                check_interval=self.check_interval,
            )
        elif self.backend == LockingBackend.REDIS:
            # Lazy import to avoid dependency for LOCAL setups
            try:
                from supertable.locking.redis_lock import RedisLocking  # type: ignore
            except Exception as e:
                raise RuntimeError(
                    "Redis backend selected, but redis backend could not be imported. "
                    "Install `redis` and ensure configuration is correct."
                ) from e

            redis_options = {
                "host": getattr(default, "REDIS_HOST", "localhost"),
                "port": getattr(default, "REDIS_PORT", 6379),
                "db": getattr(default, "REDIS_DB", 0),
                "password": getattr(default, "REDIS_PASSWORD", None),
            }
            redis_options.update(kwargs)
            self.lock_instance = RedisLocking(
                identity=identity,
                check_interval=self.check_interval,
                **redis_options,
            )
        else:
            raise ValueError(f"Unsupported locking backend: {self.backend}")

    # ---------------- Delegated public API ----------------

    def lock_resources(
        self,
        resources: Iterable[str],
        timeout_seconds: int = default.DEFAULT_TIMEOUT_SEC,
        lock_duration_seconds: int = default.DEFAULT_LOCK_DURATION_SEC,
    ) -> bool:
        return self.lock_instance.lock_resources(
            resources, timeout_seconds=timeout_seconds, lock_duration_seconds=lock_duration_seconds
        )

    def self_lock(
        self,
        timeout_seconds: int = default.DEFAULT_TIMEOUT_SEC,
        lock_duration_seconds: int = default.DEFAULT_LOCK_DURATION_SEC,
    ) -> bool:
        """
        Acquire an exclusive lock on `identity` itself.
        """
        return self.lock_instance.self_lock(
            timeout_seconds=timeout_seconds, lock_duration_seconds=lock_duration_seconds
        )

    def release_lock(self, resources: Optional[Iterable[str]] = None) -> None:
        self.lock_instance.release_lock(resources)

    # ---------------- Context manager ----------------

    def __enter__(self):
        # Important: keep this method present on this facade. Callers like
        # `with Locking(...)` rely on it. The AttributeError reported by users
        # typically comes from a different object being passed around instead of
        # this class, but we keep this explicit to avoid any ambiguity.
        if not self.self_lock():
            raise RuntimeError(f"Unable to acquire lock for {self.identity}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.release_lock()

    def __del__(self):
        try:
            self.release_lock()
        except Exception:
            pass

    # ---------------- Local shared-read helper ----------------

    def lock_shared_and_read(self, lock_file_path: str) -> Dict[str, Any]:
        """
        LOCAL/file-storage only:
          Acquire a shared (read) lock on `lock_file_path` and return parsed JSON.
          Returns {} if file is missing or invalid JSON, or locking times out.

        For non-LOCAL storage types:
          This helper is not applicable (no OS-level shared lock). Use the
          exclusive lock (`self_lock`) around your storage reads instead.
        """
        # Only applicable to LOCAL/file backend
        storage_type = getattr(default, "STORAGE_TYPE", "LOCAL").upper()
        if storage_type != "LOCAL" or self.backend != LockingBackend.FILE:
            # Fall back to the safer explicit model: caller should use exclusive
            # lock + storage.read_json; we avoid referencing undefined attributes.
            raise RuntimeError(
                "lock_shared_and_read is only supported with LOCAL file-based storage."
            )

        start_time = time.time()
        while time.time() - start_time < default.DEFAULT_TIMEOUT_SEC:
            try:
                with open(lock_file_path, "r") as fh:
                    fcntl.flock(fh, fcntl.LOCK_SH)
                    try:
                        return json.load(fh)  # type: ignore[no-any-return]
                    finally:
                        fcntl.flock(fh, fcntl.LOCK_UN)
            except BlockingIOError:
                time.sleep(self.check_interval)
            except FileNotFoundError:
                # Not created yet → return empty to indicate "no data"
                return {}
            except json.JSONDecodeError:
                # Corrupt/empty JSON → treat as empty safely
                return {}
            except OSError:
                # Another process could be rewriting/rotating the file; back off and retry
                time.sleep(self.check_interval)

        # Timed out
        return {}
