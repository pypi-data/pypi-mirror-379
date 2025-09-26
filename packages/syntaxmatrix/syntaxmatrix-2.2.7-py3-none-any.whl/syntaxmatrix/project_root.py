# syntaxmatrix/project_root.py

import os
import inspect
from pathlib import Path
import syntaxmatrix


def _is_writable(d: Path) -> bool:
    """
    Try to create the directory and a tiny test file, then remove it.
    Returns True if writes work on this path (expected for a GCS mount).
    """
    try:
        d.mkdir(parents=True, exist_ok=True)
        probe = d / ".smx_write_probe"
        with open(probe, "w", encoding="utf-8") as f:
            f.write("ok")
        try:
            probe.unlink()
        except Exception:
            pass
        return True
    except Exception:
        return False


def _caller_project_dir() -> Path:
    """
    Find the first stack frame outside the syntaxmatrix package and
    return its parent folder (best local fallback for dev).
    """
    framework_dir = Path(syntaxmatrix.__file__).resolve().parent
    for frame in inspect.stack():
        fn = frame.filename or ""
        p = Path(fn).resolve()
        try:
            p.relative_to(framework_dir)
            continue  # skip framework files
        except Exception:
            pass
        if p.exists() and p.suffix == ".py":
            return p.parent
    return Path.cwd()


def detect_project_root() -> Path:
    """
    Choose the single source-of-truth for all framework data (uploads, db, media):
      1) Honour SMX_CLIENT_DIR if provided (Cloud Run: set to /app/syntaxmatrixdir).
      2) If not set, prefer the standard Cloud Run mount path /app/syntaxmatrixdir.
      3) Otherwise fall back to a local 'syntaxmatrixdir' beside the caller (dev only).

    NOTE: We intentionally avoid using any other container paths to keep all I/O
    on the bucket mount when running on Cloud Run.
    """
    # 1) Explicit environment override
    env_dir = os.environ.get("SMX_CLIENT_DIR", "").strip()
    if env_dir:
        d = Path(env_dir).expanduser().resolve()
        if _is_writable(d):
            return d

    # 2) Default Cloud Run mount path (as used in your deploy script)
    cloud_run_mount = Path("/app/syntaxmatrixdir")
    if _is_writable(cloud_run_mount):
        return cloud_run_mount

    # 3) Dev fallback: a local folder next to the app
    local_dir = _caller_project_dir() / "syntaxmatrixdir"
    local_dir.mkdir(parents=True, exist_ok=True)
    return local_dir
