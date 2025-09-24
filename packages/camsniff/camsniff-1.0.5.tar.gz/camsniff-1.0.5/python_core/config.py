"""Central configuration helpers for CamSniff Python components.

Provides a single place to resolve output paths shared between shell and Python.

Priority order for CAMSNIFF_OUTPUT root:
1. Environment variable CAMSNIFF_OUTPUT
2. Repository relative ./output next to project root

All paths are created lazily on first access.
"""
from __future__ import annotations

from pathlib import Path
import os
from functools import lru_cache

__all__ = [
    "output_root",
    "logs_dir",
    "db_path",
    "scan_log_file",
]


@lru_cache(maxsize=1)
def _is_system_install(package_root: Path) -> bool:
    """Detect if running from a system install under /usr or /usr/local."""
    try:
        # package_root points to .../share/camsniff typically
        parent = package_root.parent
        return str(parent).startswith("/usr/share") or str(parent).startswith("/usr/local/share")
    except Exception:
        return False


@lru_cache(maxsize=1)
def output_root() -> Path:
    # 1. Explicit override
    override = os.environ.get("CAMSNIFF_OUTPUT")
    if override:
        root = Path(override)
        root.mkdir(parents=True, exist_ok=True)
        return root

    # 2. System install -> /var/lib/camsniff
    pkg_root = Path(__file__).resolve().parent.parent
    if _is_system_install(pkg_root):
        root = Path("/var/lib/camsniff")
        try:
            root.mkdir(parents=True, exist_ok=True)
        except PermissionError:
            # Fallback to user home if not privileged
            root = Path.home() / ".local" / "share" / "camsniff"
            root.mkdir(parents=True, exist_ok=True)
        return root

    # 3. Repository clone relative output
    root = pkg_root / "output"
    root.mkdir(parents=True, exist_ok=True)
    return root


def logs_dir() -> Path:
    # Use /var/log/camsniff for system install if writable
    pkg_root = Path(__file__).resolve().parent.parent
    if _is_system_install(pkg_root):
        system_log = Path("/var/log/camsniff")
        try:
            system_log.mkdir(parents=True, exist_ok=True)
            return system_log
        except PermissionError:
            pass  # fallback to output/logs
    p = output_root() / "logs"
    p.mkdir(parents=True, exist_ok=True)
    return p


def db_path() -> Path:
    p = output_root() / "results.sqlite"
    return p


def scan_log_file() -> Path:
    return logs_dir() / "scan.jsonl"
