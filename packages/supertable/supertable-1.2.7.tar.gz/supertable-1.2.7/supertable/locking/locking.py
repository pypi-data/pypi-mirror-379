import json
import time
import fcntl
import supertable.config.homedir

from supertable.config.defaults import default
from supertable.locking.file_lock import FileLocking
from supertable.locking.locking_backend import LockingBackend

class Locking:
    def __init__(
        self,
        identity,
        backend: LockingBackend = None,
        working_dir=None,
        lock_file_name=".lock.json",
        check_interval=0.1,
        **kwargs
    ):
        """
        Parameters:
            identity: Unique identifier for the lock.
            backend: Locking backend type. Defaults based on STORAGE_TYPE (LOCAL -> FILE, otherwise REDIS).
            working_dir: Directory for lock file (for FILE backend).
            lock_file_name: Name of the lock file (for FILE backend).
            check_interval: Interval to check for lock availability.
            kwargs: Additional parameters passed to the backend.
        """
        self.identity = identity
        self.check_interval = check_interval

        if backend is None:
            storage_type = getattr(default, "STORAGE_TYPE", "LOCAL").upper()
            backend = LockingBackend.FILE if storage_type == "LOCAL" else LockingBackend.REDIS

        self.backend = backend

        if self.backend == LockingBackend.REDIS:
            redis_options = {
                "host": getattr(default, "REDIS_HOST", "localhost"),
                "port": getattr(default, "REDIS_PORT", 6379),
                "db": getattr(default, "REDIS_DB", 0),
                "password": getattr(default, "REDIS_PASSWORD", None),
            }
            redis_options.update(kwargs)
            # Lazy import to avoid pulling Redis when not needed
            try:
                from supertable.locking.redis_lock import RedisLocking
            except Exception as e:
                raise RuntimeError(
                    "Redis backend selected, but redis backend could not be imported. "
                    "Install `redis` and ensure configuration is correct."
                ) from e
            self.lock_instance = RedisLocking(identity, check_interval=self.check_interval, **redis_options)

        elif self.backend == LockingBackend.FILE:
            self.lock_instance = FileLocking(
                identity,
                working_dir,
                lock_file_name=lock_file_name,
                check_interval=self.check_interval,
            )
        else:
            raise ValueError(f"Unsupported locking backend: {self.backend}")

    def lock_resources(
        self,
        resources,
        timeout_seconds=default.DEFAULT_TIMEOUT_SEC,
        lock_duration_seconds=default.DEFAULT_LOCK_DURATION_SEC
    ):
        return self.lock_instance.lock_resources(resources, timeout_seconds, lock_duration_seconds)

    def lock_resource(
        self,
        resource,
        timeout_seconds=default.DEFAULT_TIMEOUT_SEC,
        lock_duration_seconds=default.DEFAULT_LOCK_DURATION_SEC
    ):
        return self.lock_resources([resource], timeout_seconds, lock_duration_seconds)

    def extend_lock(self, duration=default.DEFAULT_LOCK_DURATION_SEC):
        return self.lock_instance.extend_lock(duration=duration)

    def release_lock(self):
        return self.lock_instance.release_lock()

    def release_resources(self, resources):
        return self.lock_instance.release_resources(resources)

    def is_locked(self, resource):
        return self.lock_instance.is_locked(resource)

    def who_locked(self, resource):
        return self.lock_instance.who_locked(resource)

    # ------------- Shared-read helper for LOCAL/REMOTE JSON -------------
    def lock_shared_and_read(self, lock_file_path):
        """
        Acquire a shared/read lock on a JSON file and read it safely.
        Works in LOCAL mode with fcntl; for REMOTE/REDIS mode it uses the backend's shared locking if available.
        Returns a dict (empty if file missing or invalid).
        """
        result = {}
        start_time = time.time()

        while time.time() - start_time < default.DEFAULT_TIMEOUT_SEC:
            if default.STORAGE_TYPE.upper() == "LOCAL":
                # 1. Local mode: use fcntl-based locking on a local file
                try:
                    with open(lock_file_path, "r") as local_file:
                        fcntl.flock(local_file, fcntl.LOCK_SH)
                        try:
                            result = json.load(local_file)
                            break
                        finally:
                            fcntl.flock(local_file, fcntl.LOCK_UN)
                except FileNotFoundError:
                    # Local file not found
                    break
                except json.JSONDecodeError:
                    # Local file has invalid JSON
                    break

            else:
                # 2. Remote/Redis mode: try to use backend’s shared lock if implemented
                try:
                    if hasattr(self, "redis_lock") and hasattr(self.redis_lock, "acquire_shared_lock"):
                        if self.redis_lock.acquire_shared_lock(lock_file_path, timeout=default.DEFAULT_TIMEOUT_SEC):
                            try:
                                # Assuming self.storage.read_json exists if you have remote storage abstraction
                                result = self.storage.read_json(lock_file_path)
                            finally:
                                self.redis_lock.release_shared_lock(lock_file_path)
                            break
                        else:
                            time.sleep(self.check_interval)
                    else:
                        # Fallback: no shared lock available, sleep and retry
                        time.sleep(self.check_interval)
                except FileNotFoundError:
                    # Path not found in remote storage
                    break
                except json.JSONDecodeError:
                    # Remote file has invalid JSON
                    break

        return result
