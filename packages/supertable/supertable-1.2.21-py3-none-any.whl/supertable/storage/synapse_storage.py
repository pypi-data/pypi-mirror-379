# supertable/storage/synapse_storage.py
# -----------------------------------------------------------------------------
# Azure Synapse activation patch for Supertable
#
# Goal
# ----
# Keep Supertable's default LOCAL behavior untouched. When running in
# Azure Synapse (or anywhere you need ABFSS/S3/GS via fsspec), call:
#
#     from supertable.storage.synapse import activate_synapse
#     activate_synapse(home="abfss://<container>@<account>.dfs.core.windows.net/<root>")
#
# This dynamically monkey-patches ONLY the necessary pieces:
#   - LocalStorage.{read_json,write_json,read_bytes,write_bytes,exists,mkdirs,size}
#   - Locking.{lock_resources,unlock_resources,lock_shared_and_read,lock_exclusive_and_write}
#
# No changes are applied until you call `activate_synapse(...)`.
# You can restore the original behavior with `deactivate_synapse()`.
#
# Why
# ---
# LocalStorage.size() in the stock implementation uses os.path.* and fails on
# cloud URIs even when the file exists. This patch routes IO through fsspec
# and fixes size()/exists() checks, while providing a cloud-safe lock.
#
# Requirements
# ------------
#   pip install fsspec adlfs
#
# -----------------------------------------------------------------------------

from __future__ import annotations

import io
import json
import os
import time
from typing import Any, Callable, Dict, Optional, Tuple

# logger (fall back to std logging if package logger not available)
try:
    from supertable.config.defaults import logger  # type: ignore
except Exception:  # pragma: no cover
    import logging

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("supertable.synapse")

# Globals to support idempotent patching and clean deactivation
_PATCHED: bool = False
_ORIG_LOCAL_STORAGE_METHODS: Dict[str, Any] = {}
_ORIG_LOCKING_METHODS: Dict[str, Any] = {}
_SUPERTABLE_HOME: Optional[str] = None


# ------------------------------- Helpers -------------------------------------


def _is_cloud_uri(p: str) -> bool:
    return isinstance(p, str) and p.startswith(
        ("abfs://", "abfss://", "s3://", "gs://", "wasbs://", "az://")
    )


def _join_uri(base: str, rel: str) -> str:
    if not rel or rel in (".", "./"):
        return base
    if _is_cloud_uri(rel):
        return rel
    return f"{base.rstrip('/')}/{rel.lstrip('/')}"


def _to_full_uri(path: str) -> str:
    """Resolve any relative/local-looking path under SUPERTABLE_HOME (cloud or local)."""
    assert _SUPERTABLE_HOME is not None, "activate_synapse() must be called first"
    if _is_cloud_uri(path):
        return path
    if _is_cloud_uri(_SUPERTABLE_HOME):
        return _join_uri(_SUPERTABLE_HOME, path)
    # If user passed a local folder as home, still resolve under it.
    return os.path.abspath(os.path.join(os.path.expanduser(_SUPERTABLE_HOME), path))


def _fs_and_path(target: str):
    """Return (fs, normalized_path) usable with fsspec."""
    import fsspec  # imported lazily when activation is requested

    fs, _, _ = fsspec.get_fs_token_paths(target)
    return fs, target


def _cloudy() -> bool:
    return _SUPERTABLE_HOME is not None and _is_cloud_uri(_SUPERTABLE_HOME)


# --------------------------- Patched implementations --------------------------


def _ls_read_json(self, path: str, retries: int = 3, backoff: float = 0.1) -> Any:
    if not _cloudy():
        return _ORIG_LOCAL_STORAGE_METHODS["read_json"](self, path)
    target = _to_full_uri(path)
    fs, norm = _fs_and_path(target)
    last_err: Optional[Exception] = None
    for _ in range(max(1, retries)):
        try:
            with fs.open(norm, "rb") as f:
                return json.load(io.TextIOWrapper(f, encoding="utf-8"))
        except FileNotFoundError:
            raise
        except Exception as e:
            last_err = e
            time.sleep(backoff)
    assert last_err is not None
    raise last_err


def _ls_write_json(self, path: str, obj: Any, retries: int = 3, backoff: float = 0.1) -> None:
    if not _cloudy():
        return _ORIG_LOCAL_STORAGE_METHODS["write_json"](self, path, obj)
    target = _to_full_uri(path)
    fs, norm = _fs_and_path(target)
    data = json.dumps(obj, ensure_ascii=False).encode("utf-8")
    last_err: Optional[Exception] = None
    for _ in range(max(1, retries)):
        try:
            parent = norm.rsplit("/", 1)[0]
            try:
                fs.mkdirs(parent, exist_ok=True)
            except Exception:
                pass
            with fs.open(norm, "wb") as f:
                f.write(data)
            return
        except Exception as e:
            last_err = e
            time.sleep(backoff)
    assert last_err is not None
    raise last_err


def _ls_read_bytes(self, path: str) -> bytes:
    if not _cloudy():
        return _ORIG_LOCAL_STORAGE_METHODS["read_bytes"](self, path)
    target = _to_full_uri(path)
    fs, norm = _fs_and_path(target)
    with fs.open(norm, "rb") as f:
        return f.read()


def _ls_write_bytes(self, path: str, data: bytes) -> None:
    if not _cloudy():
        return _ORIG_LOCAL_STORAGE_METHODS["write_bytes"](self, path, data)
    target = _to_full_uri(path)
    fs, norm = _fs_and_path(target)
    parent = norm.rsplit("/", 1)[0]
    try:
        fs.mkdirs(parent, exist_ok=True)
    except Exception:
        pass
    with fs.open(norm, "wb") as f:
        f.write(data)


def _ls_exists(self, path: str) -> bool:
    if not _cloudy():
        return _ORIG_LOCAL_STORAGE_METHODS["exists"](self, path)
    target = _to_full_uri(path)
    fs, norm = _fs_and_path(target)
    try:
        fs.info(norm)
        return True
    except FileNotFoundError:
        return False


def _ls_mkdirs(self, path: str, exist_ok: bool = True) -> None:
    if not _cloudy():
        return _ORIG_LOCAL_STORAGE_METHODS["mkdirs"](self, path, exist_ok)
    target = _to_full_uri(path)
    fs, norm = _fs_and_path(target)
    fs.mkdirs(norm, exist_ok=exist_ok)


def _ls_size(self, path: str) -> int:
    """
    Cloud-safe size(): uses fsspec metadata or a read fallback. Mirrors original
    semantics: raise FileNotFoundError when the path does not exist.
    """
    if not _cloudy():
        return _ORIG_LOCAL_STORAGE_METHODS["size"](self, path)
    target = _to_full_uri(path)
    fs, norm = _fs_and_path(target)
    try:
        if hasattr(fs, "size"):
            return int(fs.size(norm))
        info = fs.info(norm)  # raises FileNotFoundError if missing
        size_val = info.get("size")
        if size_val is not None:
            return int(size_val)
        with fs.open(norm, "rb") as f:
            return len(f.read())
    except FileNotFoundError:
        raise


# ---- Locking: use blob lock for exclusive writes; shared-read delegates to read_json


def _lockfile_for(path: str) -> str:
    return f"{path}.lock"


def _acquire_blob_lock(fs, lock_path: str, ttl_seconds: int = 300, retries: int = 30, sleep: float = 0.2) -> None:
    for _ in range(retries):
        try:
            with fs.open(lock_path, "xb") as f:  # exclusive create
                f.write(str(time.time() + ttl_seconds).encode("utf-8"))
            return
        except FileExistsError:
            try:
                with fs.open(lock_path, "rb") as f:
                    data = f.read(64)
                expiry = float(data.decode("utf-8")) if data else 0.0
            except Exception:
                expiry = 0.0
            if expiry and time.time() > expiry:
                try:
                    fs.rm(lock_path)
                    continue
                except Exception:
                    pass
            time.sleep(sleep)
    raise TimeoutError(f"Could not acquire lock: {lock_path}")


def _release_blob_lock(fs, lock_path: str) -> None:
    try:
        fs.rm(lock_path)
    except FileNotFoundError:
        pass
    except Exception:
        pass


def _lk_lock_resources(self, resource_id: str) -> None:
    # No-op in cloud mode (per-file lock used). Delegate to original locally.
    if not _cloudy():
        return _ORIG_LOCKING_METHODS["lock_resources"](self, resource_id)


def _lk_unlock_resources(self, resource_id: str) -> None:
    if not _cloudy():
        return _ORIG_LOCKING_METHODS["unlock_resources"](self, resource_id)


def _lk_lock_shared_and_read(self, path: str):
    if not _cloudy():
        return _ORIG_LOCKING_METHODS["lock_shared_and_read"](self, path)
    from supertable.storage.local_storage import LocalStorage  # type: ignore

    storage = LocalStorage()
    return storage.read_json(path)


def _lk_lock_exclusive_and_write(self, path: str, writer: Callable[[], Dict[str, Any]]):
    if not _cloudy():
        return _ORIG_LOCKING_METHODS["lock_exclusive_and_write"](self, path, writer)

    target = _to_full_uri(path)
    fs, norm = _fs_and_path(target)
    lock_path = _lockfile_for(norm)

    from supertable.storage.local_storage import LocalStorage  # type: ignore

    storage = LocalStorage()
    _acquire_blob_lock(fs, lock_path)
    try:
        obj = writer()
        storage.write_json(path, obj)
        return obj
    finally:
        _release_blob_lock(fs, lock_path)


# --------------------------- Public API (activate/deactivate) -----------------


def activate_synapse(home: Optional[str] = None) -> None:
    """
    Activate Synapse/ABFSS patching.

    Parameters
    ----------
    home : Optional[str]
        SUPERTABLE_HOME root. If a cloud URI (abfss://, s3://, ...), cloud mode
        is enabled. If a local folder, operations resolve under that folder
        (useful in Synapse when mounting local-like folders). If None, uses
        existing env SUPERTABLE_HOME or current working dir.
    """
    global _PATCHED, _SUPERTABLE_HOME

    if _PATCHED:
        logger.info("Synapse patch already active (home=%s).", _SUPERTABLE_HOME)
        return

    # Resolve home
    if home is None:
        _SUPERTABLE_HOME = os.getenv("SUPERTABLE_HOME", os.getcwd())
    else:
        _SUPERTABLE_HOME = home
        os.environ["SUPERTABLE_HOME"] = _SUPERTABLE_HOME

    # Import target classes
    try:
        import supertable.storage.local_storage as _ls  # type: ignore
        import supertable.locking.locking as _locking_mod  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise RuntimeError("Failed to import Supertable modules for patching.") from exc

    # Save originals for clean restore
    _ORIG_LOCAL_STORAGE_METHODS.update(
        {
            "read_json": getattr(_ls.LocalStorage, "read_json"),
            "write_json": getattr(_ls.LocalStorage, "write_json"),
            "read_bytes": getattr(_ls.LocalStorage, "read_bytes"),
            "write_bytes": getattr(_ls.LocalStorage, "write_bytes"),
            "exists": getattr(_ls.LocalStorage, "exists"),
            "mkdirs": getattr(_ls.LocalStorage, "mkdirs"),
            "size": getattr(_ls.LocalStorage, "size"),
        }
    )
    _ORIG_LOCKING_METHODS.update(
        {
            "lock_resources": getattr(_locking_mod.Locking, "lock_resources"),
            "unlock_resources": getattr(_locking_mod.Locking, "unlock_resources"),
            "lock_shared_and_read": getattr(_locking_mod.Locking, "lock_shared_and_read"),
            "lock_exclusive_and_write": getattr(_locking_mod.Locking, "lock_exclusive_and_write"),
        }
    )

    # Apply monkey patches
    setattr(_ls.LocalStorage, "read_json", _ls_read_json)
    setattr(_ls.LocalStorage, "write_json", _ls_write_json)
    setattr(_ls.LocalStorage, "read_bytes", _ls_read_bytes)
    setattr(_ls.LocalStorage, "write_bytes", _ls_write_bytes)
    setattr(_ls.LocalStorage, "exists", _ls_exists)
    setattr(_ls.LocalStorage, "mkdirs", _ls_mkdirs)
    setattr(_ls.LocalStorage, "size", _ls_size)

    setattr(_locking_mod.Locking, "lock_resources", _lk_lock_resources)
    setattr(_locking_mod.Locking, "unlock_resources", _lk_unlock_resources)
    setattr(_locking_mod.Locking, "lock_shared_and_read", _lk_lock_shared_and_read)
    setattr(_locking_mod.Locking, "lock_exclusive_and_write", _lk_lock_exclusive_and_write)

    _PATCHED = True

    mode = "cloud" if _cloudy() else "local-under-home"
    logger.info("Synapse patch ACTIVATED (mode=%s, home=%s).", mode, _SUPERTABLE_HOME)
    if _cloudy():
        logger.info("I/O via fsspec; locking via blob lock (*.lock).")
    else:
        logger.info("I/O remains local but resolved under SUPERTABLE_HOME.")


def deactivate_synapse() -> None:
    """
    Restore original Supertable LocalStorage and Locking methods.
    """
    global _PATCHED, _SUPERTABLE_HOME

    if not _PATCHED:
        logger.info("Synapse patch not active; nothing to deactivate.")
        return

    # Import targets
    import supertable.storage.local_storage as _ls  # type: ignore
    import supertable.locking.locking as _locking_mod  # type: ignore

    # Restore LocalStorage
    for name, func in _ORIG_LOCAL_STORAGE_METHODS.items():
        setattr(_ls.LocalStorage, name, func)

    # Restore Locking
    for name, func in _ORIG_LOCKING_METHODS.items():
        setattr(_locking_mod.Locking, name, func)

    _PATCHED = False
    logger.info("Synapse patch DEACTIVATED (home was %s).", _SUPERTABLE_HOME)


# -----------------------------------------------------------------------------
# Quiet Azure/adlfs/fsspec noisy HTTP logs
# -----------------------------------------------------------------------------
import logging
from typing import Iterable

def silence_azure_http_logs(level: int = logging.WARNING) -> None:
    """
    Suppress Azure SDK/adlfs/fsspec HTTP chatter in Synapse notebooks.

    By default sets them to WARNING, hiding INFO/DEBUG request/response noise.
    Adjust `level` to logging.ERROR or logging.CRITICAL for stricter silence.
    """
    noisy_loggers: Iterable[str] = (
        "azure",  # parent umbrella
        "azure.core.pipeline.policies.http_logging_policy",
        "azure.core.pipeline.transport",          # requests/urllib3 transport
        "azure.storage",                          # storage SDK umbrella
        "azure.storage.blob",                     # blob client logs
        "adlfs",                                  # Data Lake Filesystem wrapper
        "fsspec",                                 # filesystem shim
        "urllib3",                                # HTTP client (retries, pool)
        "aiohttp.access", "aiohttp.client",       # if async transport is used
        "chardet.charsetprober",                  # occasionally noisy
    )

    for name in noisy_loggers:
        lg = logging.getLogger(name)
        lg.setLevel(level)
        lg.propagate = False
        if not lg.handlers:
            lg.addHandler(logging.NullHandler())

    # Extra safety: ensure HttpLoggingPolicy doesn’t emit headers/queries
    try:
        from azure.core.pipeline.policies import HttpLoggingPolicy  # type: ignore
        try:
            HttpLoggingPolicy.DEFAULT_HEADERS_WHITELIST.clear()           # type: ignore[attr-defined]
            HttpLoggingPolicy.DEFAULT_QUERY_PARAMETERS_WHITELIST.clear()  # type: ignore[attr-defined]
        except Exception:
            # Fallback for older azure-core versions
            HttpLoggingPolicy.SENSITIVE_HEADERS = {"*"}              # type: ignore[attr-defined]
            HttpLoggingPolicy.SENSITIVE_QUERY_PARAMETERS = {"*"}     # type: ignore[attr-defined]
    except Exception:
        pass

    logger.info("Azure/adlfs/fsspec HTTP logs silenced at %s", logging.getLevelName(level))
