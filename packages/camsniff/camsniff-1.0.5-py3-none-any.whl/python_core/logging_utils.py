"""Unified JSONL event logging and consumption utilities.

Schema (stable v1):
{
  "ts": ISO8601 UTC string,
  "event_type": str,
  "level": str (info|warn|error|debug),
  "category": optional grouping (e.g. scan, camera, vuln),
  "message": optional human readable summary,
  "payload": object with arbitrary extra data
}

The file is append-only; each line is an independent JSON object.

Design goals:
- Atomic line appends (open/append/close) to avoid partial writes.
- Minimal dependency surface (stdlib only) so shell can call via: 
    python -m python_core.logging_utils emit --event-type camera_found --payload '{"ip":"1.2.3.4"}'
- Reader utilities for tailing and filtering.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Generator, Iterable, Optional

try:
    from . import config as _config
except Exception:  # pragma: no cover - fallback if config import fails
    _config = None  # type: ignore


EVENT_FILE_NAME = "scan.jsonl"


def _default_events_path() -> Path:
    if _config is not None:
        try:
            return Path(_config.scan_log_file())
        except Exception:
            pass
    # Fallback to local ./results directory if config unavailable
    base = Path(os.environ.get("CAM_SNIFF_OUTPUT_DIR", "results"))
    base.mkdir(parents=True, exist_ok=True)
    return base / EVENT_FILE_NAME


@dataclass
class Event:
    ts: str
    event_type: str
    level: str = "info"
    category: Optional[str] = None
    message: Optional[str] = None
    payload: Dict[str, Any] | None = None

    def to_dict(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {
            "ts": self.ts,
            "event_type": self.event_type,
            "level": self.level,
        }
        if self.category:
            data["category"] = self.category
        if self.message:
            data["message"] = self.message
        if self.payload:
            data["payload"] = self.payload
        return data


def emit_event(
    event_type: str,
    *,
    level: str = "info",
    category: str | None = None,
    message: str | None = None,
    payload: Dict[str, Any] | None = None,
    events_path: Path | None = None,
) -> None:
    """Append an event to the JSONL log."""
    if events_path is None:
        events_path = _default_events_path()
    evt = Event(
        ts=datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
        event_type=event_type,
        level=level,
        category=category,
        message=message,
        payload=payload,
    )
    line = json.dumps(evt.to_dict(), separators=(",", ":"))
    events_path.parent.mkdir(parents=True, exist_ok=True)
    with events_path.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def iter_events(
    *,
    events_path: Path | None = None,
    since_ts: str | None = None,
    event_types: Iterable[str] | None = None,
    limit: int | None = None,
) -> Generator[Dict[str, Any], None, None]:
    """Iterate events with optional filtering."""
    if events_path is None:
        events_path = _default_events_path()
    types_set = set(event_types) if event_types else None
    count = 0
    for line in events_path.open("r", encoding="utf-8") if events_path.exists() else []:
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except Exception:
            continue  # Skip malformed lines silently
        if types_set and obj.get("event_type") not in types_set:
            continue
        if since_ts and obj.get("ts") <= since_ts:
            continue
        yield obj
        count += 1
        if limit is not None and count >= limit:
            return


def tail_events(
    *,
    events_path: Path | None = None,
    follow: bool = False,
    sleep_interval: float = 0.5,
) -> Generator[Dict[str, Any], None, None]:
    """Yield events; if follow, continue streaming new lines."""
    if events_path is None:
        events_path = _default_events_path()
    pos = 0
    while True:
        if not events_path.exists():
            if follow:
                time.sleep(sleep_interval)
                continue
            else:
                return
        with events_path.open("r", encoding="utf-8") as f:
            f.seek(pos)
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    yield json.loads(line)
                except Exception:
                    continue
            pos = f.tell()
        if not follow:
            return
        time.sleep(sleep_interval)


# CLI interface -------------------------------------------------

def _cli_emit(args: argparse.Namespace) -> int:
    payload: Dict[str, Any] | None = None
    if args.payload:
        try:
            payload = json.loads(args.payload)
        except Exception:
            print("Invalid JSON for --payload", file=sys.stderr)
            return 2
    emit_event(
        args.event_type,
        level=args.level,
        category=args.category,
        message=args.message,
        payload=payload,
    )
    return 0


def _cli_tail(args: argparse.Namespace) -> int:
    limit = args.limit
    for evt in tail_events(follow=args.follow):
        print(json.dumps(evt, separators=(",", ":")))
        if limit is not None:
            limit -= 1
            if limit <= 0:
                break
    return 0


def _cli_list(args: argparse.Namespace) -> int:
    for evt in iter_events(limit=args.limit):
        print(json.dumps(evt, separators=(",", ":")))
    return 0


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m python_core.logging_utils")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_emit = sub.add_parser("emit", help="Emit a single event")
    p_emit.add_argument("--event-type", required=True)
    p_emit.add_argument("--level", default="info")
    p_emit.add_argument("--category")
    p_emit.add_argument("--message")
    p_emit.add_argument("--payload", help="Raw JSON object string")
    p_emit.set_defaults(func=_cli_emit)

    p_tail = sub.add_parser("tail", help="Tail events")
    p_tail.add_argument("--follow", action="store_true")
    p_tail.add_argument("--limit", type=int)
    p_tail.set_defaults(func=_cli_tail)

    p_list = sub.add_parser("list", help="List existing events")
    p_list.add_argument("--limit", type=int)
    p_list.set_defaults(func=_cli_list)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
