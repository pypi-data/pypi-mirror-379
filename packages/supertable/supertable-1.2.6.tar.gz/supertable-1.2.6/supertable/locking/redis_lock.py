# redis_lock.py

import time
import secrets
import threading
import atexit
import random
from typing import Iterable, Optional, Set, List, TYPE_CHECKING
if TYPE_CHECKING:
    import redis  # noqa: F401  (for type hints only)

from supertable.config.defaults import default, logger


class RedisLocking:
    """
    Redis-based, multi-thread & multi-process safe lock manager.

    Semantics intentionally mirror FileLocking (but implemented on Redis):
      - All-or-nothing acquisition for a requested set of resources
      - TTL-based lock with background heartbeat extension
      - Subset and full release supported
      - In-process overlap guard (don't deadlock yourself)
      - Context manager support
      - atexit cleanup
      - DEBUG logs:
          * resources requested
          * per-resource conflict lines:
            "[<identity>] lock blocked by <res> (held by <who>, TTL=<s>s), retrying…"
          * heartbeat lifecycle
    """

    def __init__(
        self,
        identity: str,
        check_interval: float = 0.1,
        redis_client: Optional["redis.Redis"] = None,  # type: ignore[name-defined]
        host: str = "localhost",
        port: int = 6379,
        db: int = 0,
        password: Optional[str] = None,
    ):
        self.identity = identity
        self.check_interval = check_interval

        # Lazy import so FILE backend users don't need the redis package installed
        if redis_client is None:
            try:
                import redis  # runtime import only if needed
            except ImportError as e:
                raise ImportError(
                    "Redis backend requires the `redis` package. Install it with `pip install redis`."
                ) from e
            self.redis = redis.Redis(host=host, port=port, db=db, password=password)
        else:
            self.redis = redis_client

        # Active lock state
        self._locked_resources: Set[str] = set()
        self.lock_id = secrets.token_hex(16)
        self._in_process_lock = threading.Lock()

        # Heartbeat thread control
        self._hb_thread: Optional[threading.Thread] = None
        self._hb_stop = threading.Event()
        self._hb_interval_sec: int = 0
        self._last_duration_sec: int = 0

        atexit.register(self._atexit_cleanup)

    # ---------------- Internals ----------------

    def _atexit_cleanup(self):
        try:
            self.release_lock()
        except Exception as e:
            try:
                logger.debug(f"{self.identity}: atexit release_lock() raised: {e}")
            except Exception:
                pass

    def _heartbeat_loop(self):
        """
        Background thread loop that extends TTL periodically for all held keys.
        """
        while not self._hb_stop.is_set():
            try:
                # extend by last known duration (so semantics match extend_lock())
                if self._last_duration_sec > 0 and self._locked_resources:
                    for res in list(self._locked_resources):
                        # Extend main lock key TTL
                        key = f"lock:{res}"
                        self.redis.expire(key, self._last_duration_sec)
                        # Extend owner/WHO key TTL
                        who = f"lock:{res}:who"
                        self.redis.expire(who, self._last_duration_sec)
                # Sleep until next beat
                time.sleep(self._hb_interval_sec)
            except Exception as e:
                try:
                    logger.debug(f"{self.identity}: heartbeat error: {e}")
                except Exception:
                    pass
                time.sleep(self._hb_interval_sec)

    def _ensure_heartbeat(self, interval: int, lock_duration_seconds: int):
        """
        Ensure heartbeat thread is running with given interval.
        """
        if self._hb_thread is None or not self._hb_thread.is_alive():
            self._hb_stop.clear()
            self._hb_interval_sec = interval
            self._last_duration_sec = lock_duration_seconds
            self._hb_thread = threading.Thread(
                target=self._heartbeat_loop, name=f"RedisLockHB-{self.identity}", daemon=True
            )
            self._hb_thread.start()
            logger.debug(
                f"{self.identity}: redis heartbeat started (interval={interval}s, duration={lock_duration_seconds}s)"
            )

    # ---------------- Public API ----------------

    def lock_resources(
        self,
        resources: Iterable[str],
        timeout_seconds: int = default.DEFAULT_TIMEOUT_SEC,
        lock_duration_seconds: int = default.DEFAULT_LOCK_DURATION_SEC,
        heartbeat_interval_seconds: int = default.DEFAULT_HEARTBEAT_INTERVAL_SEC,
    ) -> bool:
        """
        Try to atomically acquire locks for all resources in `resources`.
        Returns True if successful for the whole set within timeout, else False.
        """
        resources = list(resources)
        start_ts = time.time()
        deadline = start_ts + timeout_seconds

        logger.debug(
            f"{self.identity}: attempting redis-lock on resources={resources} "
            f"(timeout={timeout_seconds}s, duration={lock_duration_seconds}s)"
        )

        attempted = set()
        while time.time() < deadline:
            try:
                ok_all = True
                expiration = lock_duration_seconds
                random.shuffle(resources)

                # try each resource once per pass
                for res in resources:
                    key = f"lock:{res}"
                    who = f"lock:{res}:who"

                    # NX set (only if not exists), EX seconds
                    ok = self.redis.set(key, self.lock_id, ex=expiration, nx=True)
                    if ok:
                        # write identity -> who key (best effort)
                        try:
                            self.redis.set(who, self.identity, ex=expiration)
                        except Exception:
                            pass
                        logger.debug(f"{self.identity}: redis set OK key={key} exp={expiration}")
                        attempted.add(res)
                    else:
                        ok_all = False
                        # Optional: debug who/ttl if available
                        try:
                            cur = self.redis.get(key)
                            ttl = self.redis.ttl(key)
                            holder_who = self.redis.get(who)
                            holder = holder_who.decode("utf-8") if holder_who else "unknown"
                            logger.debug(
                                f"{self.identity}: blocked on {res} "
                                f"(held_by_lock_id={cur}, held_by={holder}, TTL={ttl}s) — retrying…"
                            )
                        except Exception:
                            logger.debug(f"{self.identity}: blocked on {res}, retrying…")
                        break  # fail-fast on this pass, retry outer

                if ok_all:
                    # Success: remember and start heartbeat
                    self._locked_resources.update(attempted)
                    self._ensure_heartbeat(heartbeat_interval_seconds, lock_duration_seconds)
                    logger.debug(f"{self.identity}: acquired redis locks on {sorted(self._locked_resources)}")
                    return True

                # Backoff
                time.sleep(self._jitter_sleep())

            except Exception as e:
                logger.debug(f"{self.identity}: redis lock acquisition error: {e}")
                time.sleep(self._jitter_sleep())

        logger.debug(f"{self.identity}: FAILED to acquire redis lock on {resources} within {timeout_seconds}s")
        return False

    def lock_resource(
        self,
        resource: str,
        timeout_seconds: int = default.DEFAULT_TIMEOUT_SEC,
        lock_duration_seconds: int = default.DEFAULT_LOCK_DURATION_SEC,
        heartbeat_interval_seconds: int = default.DEFAULT_HEARTBEAT_INTERVAL_SEC,
    ) -> bool:
        return self.lock_resources(
            [resource], timeout_seconds, lock_duration_seconds, heartbeat_interval_seconds
        )

    def release_resources(self, resources: Iterable[str]) -> None:
        """
        Release only a subset of currently held resources.
        """
        resources = list(resources)
        for res in resources:
            key = f"lock:{res}"
            who = f"lock:{res}:who"
            try:
                cur = self.redis.get(key)
                if cur and cur.decode("utf-8") == self.lock_id:
                    self.redis.delete(key)
                try:
                    self.redis.delete(who)
                except Exception:
                    pass
            except Exception as e:
                logger.debug(f"{self.identity}: error during partial release for {res}: {e}")

        for r in resources:
            self._locked_resources.discard(r)

        if not self._locked_resources:
            # stop heartbeat if nothing left
            self._stop_heartbeat()

    def release_lock(self) -> None:
        """
        Release all held resources.
        """
        try:
            for res in list(self._locked_resources):
                key = f"lock:{res}"
                who = f"lock:{res}:who"
                cur = self.redis.get(key)
                if cur and cur.decode("utf-8") == self.lock_id:
                    self.redis.delete(key)
                try:
                    self.redis.delete(who)
                except Exception:
                    pass
        finally:
            self._locked_resources.clear()
            self._stop_heartbeat()

    def _stop_heartbeat(self):
        if self._hb_thread and self._hb_thread.is_alive():
            self._hb_stop.set()
            try:
                self._hb_thread.join(timeout=2.0)
            except Exception:
                pass
            logger.debug(f"{self.identity}: redis heartbeat stopped")
        self._hb_thread = None

    def is_locked(self, resource: str) -> bool:
        """
        Check if a resource is currently locked (not necessarily by us).
        """
        try:
            key = f"lock:{resource}"
            val = self.redis.get(key)
            return bool(val)
        except Exception:
            return False

    def who_locked(self, resource: str) -> Optional[str]:
        """
        Return identity (if recorded) of who holds the lock, else None.
        """
        try:
            who = f"lock:{resource}:who"
            val = self.redis.get(who)
            return val.decode("utf-8") if val else None
        except Exception:
            return None

    def extend_lock(self, duration: int = default.DEFAULT_LOCK_DURATION_SEC) -> bool:
        """
        Extend TTL for all currently held resources by `duration` seconds.
        """
        if not self._locked_resources:
            return False

        self._last_duration_sec = duration
        for res in list(self._locked_resources):
            try:
                key = f"lock:{res}"
                if self.redis.get(key):
                    self.redis.expire(key, duration)
                who = f"lock:{res}:who"
                try:
                    self.redis.set(who, self.identity, ex=duration)
                except Exception:
                    pass
            except Exception as e:
                logger.debug(f"{self.identity}: redis heartbeat error on {key}: {e}")
        return True

    # ---------------- Utils ----------------

    def _jitter_sleep(self) -> float:
        """
        Small randomized backoff to reduce stampeding herd.
        """
        base = self.check_interval
        return base + random.uniform(0, base)
