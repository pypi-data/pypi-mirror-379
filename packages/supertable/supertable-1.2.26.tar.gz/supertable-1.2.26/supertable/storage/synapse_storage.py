# supertable/storage/synapse_storage.py
# -----------------------------------------------------------------------------
# One-call activation for Synapse / ABFSS:
#   - All LocalStorage I/O (json/bytes/ls/size/delete/parquet) via fsspec+adlfs.
#   - Polars .write_parquet -> fsspec+pyarrow (no recursion).
#   - DataReader -> caches Parquet locally then uses a *pristine* DuckDB.
#   - MonitoringLogger/MonitoringReader -> same ABFSS-safe behaviors.
#
# Usage:
#   from supertable.storage.synapse_storage import activate_synapse, silence_azure_http_logs
#   activate_synapse(home="abfss://<acct>@<fs>.dfs.core.windows.net/supertable")
#   silence_azure_http_logs(logging.INFO)
# -----------------------------------------------------------------------------

from __future__ import annotations

import io
import json
import os
import sys
import tempfile
import time
import traceback
from typing import Any, Callable, Dict, Iterable, List, Optional

# Public API
__all__ = ["activate_synapse", "silence_azure_http_logs"]

# ---------- Module state (idempotency guard) ----------
_PATCHED = False


# ============================ Public: logging helper ============================

def silence_azure_http_logs(level: int = __import__("logging").WARNING) -> None:
    """
    Suppress Azure SDK/adlfs/fsspec HTTP chatter (INFO/DEBUG) without muting your app logs.
    """
    import logging
    noisy_loggers: Iterable[str] = (
        "azure",
        "azure.core.pipeline.policies.http_logging_policy",
        "azure.core.pipeline.transport",
        "azure.storage",
        "azure.storage.blob",
        "adlfs",
        "fsspec",
        "urllib3",
        "aiohttp.access", "aiohttp.client",
        "chardet.charsetprober",
    )
    for name in noisy_loggers:
        lg = logging.getLogger(name)
        lg.setLevel(level)
        lg.propagate = False
        if not lg.handlers:
            lg.addHandler(logging.NullHandler())

    # Extra safety: disable HttpLoggingPolicy header/query whitelists
    try:
        from azure.core.pipeline.policies import HttpLoggingPolicy  # type: ignore
        try:
            HttpLoggingPolicy.DEFAULT_HEADERS_WHITELIST.clear()          # type: ignore[attr-defined]
            HttpLoggingPolicy.DEFAULT_QUERY_PARAMETERS_WHITELIST.clear()  # type: ignore[attr-defined]
        except Exception:
            # Older azure-core
            HttpLoggingPolicy.SENSITIVE_HEADERS = {"*"}              # type: ignore[attr-defined]
            HttpLoggingPolicy.SENSITIVE_QUERY_PARAMETERS = {"*"}     # type: ignore[attr-defined]
    except Exception:
        pass


# ============================ Public: activation ============================

def activate_synapse(
    home: Optional[str] = None,
    *,
    cache_dir: Optional[str] = None,
    duckdb_memory_limit: str = "2GB",
) -> None:
    """
    Patch Supertable to run reliably on Azure Synapse (ABFSS).

    - home: ABFSS root for Supertable (e.g., 'abfss://.../supertable').
    - cache_dir: local directory for DuckDB parquet cache (default: /tmp/supertable_duck_cache).
    - duckdb_memory_limit: PRAGMA memory_limit value (e.g., '2GB').

    Idempotent: safe to call more than once.
    """
    global _PATCHED
    if _PATCHED:
        return

    # ---------- Configure homes/paths ----------
    if home:
        os.environ["SUPERTABLE_HOME"] = home
    SUPERTABLE_HOME = os.getenv("SUPERTABLE_HOME", home or "")
    if not SUPERTABLE_HOME:
        raise ValueError("activate_synapse(home=...) is required (ABFSS path).")

    if cache_dir:
        os.environ["SUPERTABLE_LOCAL_CACHE"] = cache_dir
    LOCAL_CACHE_DIR = os.environ.get(
        "SUPERTABLE_LOCAL_CACHE",
        os.path.join(tempfile.gettempdir(), "supertable_duck_cache"),
    )
    os.makedirs(LOCAL_CACHE_DIR, exist_ok=True)

    # ---------- App logger (reuse Supertable's logger if present) ----------
    try:
        from supertable.config.defaults import logger  # type: ignore
    except Exception:
        import logging
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger("supertable.synapse")

    # ---------- Dependencies ----------
    try:
        import fsspec  # noqa: F401
    except Exception as exc:
        raise RuntimeError(
            "fsspec/adlfs/pyarrow are required.\nInstall:\n  %pip install fsspec adlfs pyarrow polars duckdb"
        ) from exc
    try:
        import adlfs  # noqa: F401
    except Exception:
        pass
    try:
        import pyarrow as pa  # noqa: F401
        import pyarrow.parquet as pq  # noqa: F401
    except Exception as exc:
        raise RuntimeError("pyarrow is required. Install: %pip install pyarrow") from exc
    try:
        import polars as _pl  # noqa: F401
    except Exception as exc:
        raise RuntimeError("polars is required. Install: %pip install polars") from exc
    import importlib

    # ---------- Helper funcs ----------

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
        homev = os.getenv("SUPERTABLE_HOME", SUPERTABLE_HOME)
        if _is_cloud_uri(path):
            return path
        if _is_cloud_uri(homev):
            return _join_uri(homev, path)
        return os.path.abspath(os.path.join(os.path.expanduser(homev), path))

    def _fs_and_path(target: str):
        import fsspec as _fs
        fs, _, _ = _fs.get_fs_token_paths(target)
        return fs, target

    def _file_size(path: str) -> int:
        try:
            return os.path.getsize(path)
        except Exception:
            return -1

    def _ensure_local_copy_verbose(path_like: str) -> str:
        """
        Resolve a (relative or abfss://) Parquet path to a local cached copy.
        Deterministic name by SHA1 of the *full* URI.
        """
        import hashlib
        target = _to_full_uri(path_like)
        os.makedirs(LOCAL_CACHE_DIR, exist_ok=True)
        local_name = hashlib.sha1(target.encode("utf-8")).hexdigest() + ".parquet"
        local_path = os.path.join(LOCAL_CACHE_DIR, local_name)

        if os.path.exists(local_path):
            logger.debug(f"[reader.cache] HIT  → {path_like} → {local_path} ({_file_size(local_path)} bytes)")
            return local_path

        fs, norm = _fs_and_path(target)
        logger.debug(f"[reader.cache] MISS → opening {norm} via {fs.__class__.__name__}")
        try:
            with fs.open(norm, "rb") as src, open(local_path, "wb") as dst:
                copied = 0
                while True:
                    chunk = src.read(8 * 1024 * 1024)
                    if not chunk:
                        break
                    dst.write(chunk)
                    copied += len(chunk)
            logger.debug(f"[reader.cache] WROTE {copied} bytes → {local_path}")
        except Exception:
            logger.error(f"[reader.cache] FAILED copying {norm} → {local_path}")
            logger.error(traceback.format_exc())
            raise
        return local_path

    def _get_pristine_duckdb():
        """Ensure we use an unwrapped duckdb module (defensive reload)."""
        mod = sys.modules.get("duckdb")
        if mod is None:
            import duckdb as _duckdb  # type: ignore
            mod = _duckdb
        connect = getattr(mod, "connect", None)
        if not callable(connect) or getattr(connect, "__module__", "") != "duckdb":
            logger.debug("[reader.patch] Detected monkeypatched duckdb.connect → reloading duckdb")
            mod = importlib.reload(mod)
        return mod

    # ===================== Patch 1: LocalStorage via fsspec/adlfs =====================

    try:
        import supertable.storage.local_storage as _ls  # type: ignore
    except Exception as exc:
        raise RuntimeError("Could not import supertable.storage.local_storage to patch.") from exc

    import pyarrow as pa
    import pyarrow.parquet as pq

    _ORIG_read_json = getattr(_ls.LocalStorage, "read_json", None)
    _ORIG_write_json = getattr(_ls.LocalStorage, "write_json", None)
    _ORIG_read_bytes = getattr(_ls.LocalStorage, "read_bytes", None)
    _ORIG_write_bytes = getattr(_ls.LocalStorage, "write_bytes", None)
    _ORIG_exists = getattr(_ls.LocalStorage, "exists", None)
    _ORIG_mkdirs = getattr(_ls.LocalStorage, "makedirs", None)
    _ORIG_size = getattr(_ls.LocalStorage, "size", None)
    _ORIG_delete = getattr(_ls.LocalStorage, "delete", None)
    _ORIG_list_files = getattr(_ls.LocalStorage, "list_files", None)
    _ORIG_get_dir = getattr(_ls.LocalStorage, "get_directory_structure", None)
    _ORIG_write_parquet = getattr(_ls.LocalStorage, "write_parquet", None)
    _ORIG_read_parquet = getattr(_ls.LocalStorage, "read_parquet", None)

    def _cloudy() -> bool:
        return _is_cloud_uri(os.getenv("SUPERTABLE_HOME", SUPERTABLE_HOME))

    def _ls_read_json(self, path: str, retries: int = 3, backoff: float = 0.05) -> Any:
        if not _cloudy() and _ORIG_read_json:
            return _ORIG_read_json(self, path)
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

    def _ls_write_json(self, path: str, obj: Any, retries: int = 3, backoff: float = 0.05) -> None:
        if not _cloudy() and _ORIG_write_json:
            return _ORIG_write_json(self, path, obj)
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
        if not _cloudy() and _ORIG_read_bytes:
            return _ORIG_read_bytes(self, path)
        fs, norm = _fs_and_path(_to_full_uri(path))
        with fs.open(norm, "rb") as f:
            return f.read()

    def _ls_write_bytes(self, path: str, data: bytes) -> None:
        if not _cloudy() and _ORIG_write_bytes:
            return _ORIG_write_bytes(self, path, data)
        fs, norm = _fs_and_path(_to_full_uri(path))
        parent = norm.rsplit("/", 1)[0]
        try:
            fs.mkdirs(parent, exist_ok=True)
        except Exception:
            pass
        with fs.open(norm, "wb") as f:
            f.write(data)

    def _ls_exists(self, path: str) -> bool:
        if not _cloudy() and _ORIG_exists:
            return _ORIG_exists(self, path)
        fs, norm = _fs_and_path(_to_full_uri(path))
        try:
            return fs.exists(norm)
        except Exception:
            try:
                fs.info(norm)
                return True
            except Exception:
                return False

    def _ls_mkdirs(self, path: str) -> None:
        if not _cloudy() and _ORIG_mkdirs:
            return _ORIG_mkdirs(self, path)
        fs, norm = _fs_and_path(_to_full_uri(path))
        try:
            fs.mkdirs(norm, exist_ok=True)
        except Exception:
            pass

    def _ls_size(self, path: str) -> int:
        if not _cloudy() and _ORIG_size:
            return _ORIG_size(self, path)
        fs, norm = _fs_and_path(_to_full_uri(path))
        try:
            if hasattr(fs, "size"):
                return int(fs.size(norm))
            info = fs.info(norm)
            size_val = info.get("size")
            if size_val is None:
                with fs.open(norm, "rb") as f:
                    return len(f.read())
            return int(size_val)
        except FileNotFoundError:
            raise

    def _ls_delete(self, path: str) -> None:
        if not _cloudy() and _ORIG_delete:
            return _ORIG_delete(self, path)
        fs, norm = _fs_and_path(_to_full_uri(path))
        try:
            fs.rm(norm, recursive=True)
        except FileNotFoundError:
            raise

    def _ls_list_files(self, path: str, pattern: str = "*") -> List[str]:
        if not _cloudy() and _ORIG_list_files:
            return _ORIG_list_files(self, path, pattern)
        fs, norm = _fs_and_path(_to_full_uri(path))
        try:
            return fs.glob(f"{norm.rstrip('/')}/{pattern}")
        except Exception:
            try:
                return [entry["name"] for entry in fs.ls(norm)]
            except Exception:
                return []

    def _ls_get_directory_structure(self, path: str) -> dict:
        if not _cloudy() and _ORIG_get_dir:
            return _ORIG_get_dir(self, path)
        fs, norm = _fs_and_path(_to_full_uri(path))
        result: Dict[str, Any] = {}

        def _recurse(prefix: str, node: dict):
            try:
                entries = fs.ls(prefix, detail=True)
            except FileNotFoundError:
                return
            for e in entries:
                name = e.get("name") or e.get("Key") or ""
                key = name.rstrip("/").split("/")[-1]
                if e.get("type") == "directory" or name.endswith("/"):
                    node[key] = {}
                    _recurse(name, node[key])
                else:
                    node[key] = None

        _recurse(norm, result)
        return result

    def _ls_write_parquet(self, table: pa.Table, path: str) -> None:
        if not _cloudy() and _ORIG_write_parquet:
            return _ORIG_write_parquet(self, table, path)
        fs, norm = _fs_and_path(_to_full_uri(path))
        parent = norm.rsplit("/", 1)[0]
        try:
            fs.mkdirs(parent, exist_ok=True)
        except Exception:
            pass
        with fs.open(norm, "wb") as f:
            pq.write_table(table, f)

    def _ls_read_parquet(self, path: str) -> pa.Table:
        if not _cloudy() and _ORIG_read_parquet:
            return _ORIG_read_parquet(self, path)
        fs, norm = _fs_and_path(_to_full_uri(path))
        with fs.open(norm, "rb") as f:
            return pq.read_table(f)

    # Apply LocalStorage patches
    setattr(_ls.LocalStorage, "read_json", _ls_read_json)
    setattr(_ls.LocalStorage, "write_json", _ls_write_json)
    setattr(_ls.LocalStorage, "read_bytes", _ls_read_bytes)
    setattr(_ls.LocalStorage, "write_bytes", _ls_write_bytes)
    setattr(_ls.LocalStorage, "exists", _ls_exists)
    setattr(_ls.LocalStorage, "makedirs", _ls_mkdirs)
    setattr(_ls.LocalStorage, "size", _ls_size)
    setattr(_ls.LocalStorage, "delete", _ls_delete)
    setattr(_ls.LocalStorage, "list_files", _ls_list_files)
    setattr(_ls.LocalStorage, "get_directory_structure", _ls_get_directory_structure)
    setattr(_ls.LocalStorage, "write_parquet", _ls_write_parquet)
    setattr(_ls.LocalStorage, "read_parquet", _ls_read_parquet)

    # ===================== Patch 2: Polars write_parquet =====================

    import polars as pl
    _PL_ORIG_WRITE_PARQUET = getattr(pl.DataFrame, "write_parquet", None)

    def _already_wrapped(func: Callable[..., Any]) -> bool:
        return getattr(func, "__supertable_cloud_wrapped__", False) is True

    def _cloudsafe_pl_write_parquet(self, *args, **kwargs):
        file_arg: Optional[Any] = None
        if "file" in kwargs:
            file_arg = kwargs["file"]
        elif args:
            file_arg = args[0]

        # Buffer/file-like → delegate to original if present
        if not isinstance(file_arg, str):
            if _PL_ORIG_WRITE_PARQUET and not _already_wrapped(_PL_ORIG_WRITE_PARQUET):
                return _PL_ORIG_WRITE_PARQUET(self, *args, **kwargs)
            table = self.to_arrow()
            sink = file_arg
            compression = kwargs.get("compression", "zstd")
            compression_level = kwargs.get("compression_level", None)
            pq.write_table(table, sink, compression=compression, compression_level=compression_level)
            return

        # String path → fsspec+pyarrow
        target = _to_full_uri(file_arg)
        compression = kwargs.get("compression", "zstd")
        compression_level = kwargs.get("compression_level", None)

        table = self.to_arrow()
        fs, norm = _fs_and_path(target)
        parent = norm.rsplit("/", 1)[0]
        try:
            fs.mkdirs(parent, exist_ok=True)
        except Exception:
            pass
        with fs.open(norm, "wb") as f:
            pq.write_table(table, f, compression=compression, compression_level=compression_level)
        return None

    if _PL_ORIG_WRITE_PARQUET is not None and not _already_wrapped(_PL_ORIG_WRITE_PARQUET):
        setattr(_cloudsafe_pl_write_parquet, "__supertable_cloud_wrapped__", True)
        setattr(pl.DataFrame, "write_parquet", _cloudsafe_pl_write_parquet)

    # ===================== Patch 3: DataReader (cache parquet + pristine DuckDB) =====================

    try:
        import supertable.data_reader as _dr  # type: ignore
    except Exception as exc:
        raise RuntimeError("Could not import supertable.data_reader to patch.") from exc

    _ORIG_execute_with_duckdb = getattr(_dr.DataReader, "execute_with_duckdb", None)

    def _patched_execute_with_duckdb(self, parquet_files, query_manager):
        """Replace remote paths with local cached copies and run DuckDB. Verbose logs."""
        logger.debug(self._lp(f"[reader.patch] activate execute_with_duckdb, files={len(parquet_files)}"))
        try:
            local_files: List[str] = []
            for p in parquet_files:
                lp = _ensure_local_copy_verbose(p)
                local_files.append(lp)
            for src, dst in zip(parquet_files, local_files):
                logger.debug(self._lp(f"[reader.paths] {src}  ->  {dst}  ({_file_size(dst)} bytes)"))

            _duckdb = _get_pristine_duckdb()
            logger.debug(self._lp(f"[duckdb] using module={_duckdb!r}, connect={getattr(_duckdb, 'connect', None)!r}"))
            con = _duckdb.connect()

            try:
                self.timer.capture_and_reset_timing("CONNECTING")

                pragmas = [
                    f"PRAGMA memory_limit='{duckdb_memory_limit}';",
                    f"PRAGMA temp_directory='{query_manager.temp_dir}';",
                    "PRAGMA enable_profiling='json';",
                    f"PRAGMA profile_output = '{query_manager.query_plan_path}';",
                    "PRAGMA default_collation='nocase';",
                ]
                for p in pragmas:
                    logger.debug(self._lp(f"[duckdb] {p.strip()}"))
                    con.execute(p)

                parquet_files_str = ", ".join(f"'{f}'" for f in local_files)
                if self.parser.columns_csv == "*":
                    safe_columns_csv = "*"
                else:
                    def _q(c: str) -> str:
                        c = c.strip()
                        if c == "*":
                            return "*"
                        if all(ch.isalnum() or ch == "_" for ch in c):
                            return c
                        return '"' + c.replace('"', '""') + '"'
                    safe_columns_csv = ", ".join(_q(c) for c in self.parser.columns_list)

                create_table = f"""
CREATE TABLE {self.parser.reflection_table}
AS
SELECT {safe_columns_csv}
FROM parquet_scan([{parquet_files_str}], union_by_name=TRUE, HIVE_PARTITIONING=TRUE);
""".strip()
                logger.debug(self._lp("[duckdb] CREATE TABLE SQL ↓"))
                logger.debug(self._lp(create_table))
                con.execute(create_table)

                create_view = f"""
CREATE VIEW {self.parser.rbac_view}
AS
{self.parser.view_definition}
""".strip()
                logger.debug(self._lp("[duckdb] CREATE VIEW SQL ↓"))
                logger.debug(self._lp(create_view))
                con.execute(create_view)

                self.timer.capture_and_reset_timing("CREATING_REFLECTION")
                logger.debug(self._lp(f"[duckdb] Executing final query: {self.parser.executing_query}"))
                result = con.execute(query=self.parser.executing_query).fetchdf()
                logger.debug(self._lp(f"[duckdb] result: rows={result.shape[0]}, cols={result.shape[1]}"))
                return result
            finally:
                try:
                    con.close()
                except Exception:
                    pass

        except Exception:
            logger.error(self._lp("[reader.patch] Unhandled exception:"))
            logger.error(self._lp(traceback.format_exc()))
            raise

    if _ORIG_execute_with_duckdb is not None:
        setattr(_dr.DataReader, "execute_with_duckdb", _patched_execute_with_duckdb)

    # ===================== Patch 4: MonitoringLogger (merge via storage) =====================

    try:
        import supertable.monitoring_logger as _ml  # type: ignore
    except Exception as exc:
        raise RuntimeError("Could not import supertable.monitoring_logger to patch.") from exc

    _ORIG_ML_write_parquet_file = getattr(_ml.MonitoringLogger, "_write_parquet_file", None)

    def _patched_ml_write_parquet_file(self, data: List[Dict[str, Any]], existing_path: Optional[str] = None) -> Dict[str, Any]:
        import polars as pl  # local import to avoid hard dep if not used
        if not data:
            return {
                "file": existing_path or "",
                "file_size": 0,
                "rows": 0,
                "columns": 0,
                "stats": {}
            }

        logger.debug(f"[monitoring.logger] incoming batch size={len(data)} existing_path={existing_path}")
        data = [self._ensure_execution_time(record) for record in data]
        df = pl.from_dicts(data)

        if existing_path and self.storage.exists(existing_path):
            try:
                logger.debug(f"[monitoring.logger] merging into existing file: {existing_path}")
                existing_table = self.storage.read_parquet(existing_path)  # pyarrow.Table
                existing_df = pl.from_arrow(existing_table)
                df = pl.concat([existing_df, df], how="vertical_relaxed")
                self.storage.delete(existing_path)
            except Exception as e:
                logger.warning(f"Warning: Failed to merge with existing file {existing_path}: {str(e)}")

        new_filename = self._generate_filename("data.parquet")
        new_path = os.path.join(self.data_dir, new_filename)

        table = df.to_arrow()
        logger.debug(f"[monitoring.logger] writing parquet rows={len(df)} cols={len(df.columns)} → {new_path}")
        self.storage.write_parquet(table, new_path)

        resource = {
            "file": new_path,
            "file_size": self.storage.size(new_path),
            "rows": len(df),
            "columns": len(df.columns),
            "stats": self._calculate_stats(df)
        }
        logger.debug(f"[monitoring.logger] wrote parquet resource={resource}")
        return resource

    if _ORIG_ML_write_parquet_file is not None:
        setattr(_ml.MonitoringLogger, "_write_parquet_file", _patched_ml_write_parquet_file)

    # ===================== Patch 5: MonitoringReader (cache parquet + pristine DuckDB) =====================

    try:
        import supertable.monitoring_reader as _mr  # type: ignore
    except Exception as exc:
        raise RuntimeError("Could not import supertable.monitoring_reader to patch.") from exc

    _ORIG_MR_read = getattr(_mr.MonitoringReader, "read", None)

    def _patched_mr_read(self, from_ts_ms: Optional[int] = None, to_ts_ms: Optional[int] = None, limit: int = 1000):
        import pandas as pd
        from datetime import datetime, timezone, timedelta

        now_ms = int(datetime.now(timezone.utc).timestamp() * 1_000)
        if to_ts_ms is None:
            to_ts_ms = now_ms
        if from_ts_ms is None:
            from_ts_ms = to_ts_ms - int(timedelta(days=1).total_seconds() * 1_000)
        if from_ts_ms > to_ts_ms:
            raise ValueError(f"from_ts_ms ({from_ts_ms}) must be <= to_ts_ms ({to_ts_ms})")

        snapshot = self._load_current_snapshot()
        parquet_files = self._collect_parquet_files(snapshot, from_ts_ms, to_ts_ms)
        if not parquet_files:
            logger.debug("[monitoring.reader] No parquet files match time window.")
            return pd.DataFrame()

        local_files: List[str] = []
        for p in parquet_files:
            lp = _ensure_local_copy_verbose(p)
            local_files.append(lp)
            logger.debug(f"[monitoring.reader.paths] {p} -> {lp} ({_file_size(lp)} bytes)")

        _duckdb = _get_pristine_duckdb()
        con = _duckdb.connect()
        con.execute(f"PRAGMA memory_limit='{duckdb_memory_limit}';")
        con.execute(f"PRAGMA temp_directory='{self.temp_dir}';")
        con.execute("PRAGMA default_collation='nocase';")

        files_sql_array = "[" + ", ".join(f"'{f}'" for f in local_files) + "]"
        query = (
            "SELECT *\n"
            f"FROM parquet_scan({files_sql_array}, union_by_name=TRUE, HIVE_PARTITIONING=TRUE)\n"
            f"WHERE execution_time BETWEEN {from_ts_ms} AND {to_ts_ms}\n"
            "ORDER BY execution_time DESC\n"
            f"LIMIT {limit}"
        )
        logger.debug("[monitoring.reader] Executing Query:\n%s", query)

        try:
            df = con.execute(query).fetchdf()
        finally:
            try:
                con.close()
            except Exception:
                pass

        logger.debug("[monitoring.reader] Result shape: %s", df.shape)
        return df

    if _ORIG_MR_read is not None:
        setattr(_mr.MonitoringReader, "read", _patched_mr_read)

    # ---------- Final log ----------
    logger.info("Supertable Synapse/ABFSS patches activated.")
    logger.info("  SUPERTABLE_HOME = %s", os.getenv("SUPERTABLE_HOME"))
    logger.info("  LOCAL_CACHE_DIR = %s", LOCAL_CACHE_DIR)
    logger.info("  DuckDB memory_limit = %s", duckdb_memory_limit)

    _PATCHED = True
