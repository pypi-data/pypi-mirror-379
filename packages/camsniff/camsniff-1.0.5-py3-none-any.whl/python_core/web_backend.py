"""Lightweight FastAPI backend exposing CamSniff scan events.

Features:
 - Root HTML page with live WebSocket log viewer
 - /health simple readiness probe
 - /events tail last N structured JSONL events (filtered optionally by level/event)
 - /ws streaming incremental tail (efficient, no full file read each loop)

Assumptions:
 - Scan JSONL file produced by bash core is located under output/logs/scan.jsonl
 - Environment variable CAMSNIFF_OUTPUT can override base output dir
"""

from __future__ import annotations

import asyncio
import json
import os
from pathlib import Path
from typing import AsyncGenerator, List, Optional

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Query
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
import uvicorn

from . import logging_utils

# Resolve output base early; fallback to repo-relative path
OUTPUT_BASE = Path(os.environ.get("CAMSNIFF_OUTPUT", Path(__file__).resolve().parent.parent / "output"))
LOG_FILE = OUTPUT_BASE / "logs" / "scan.jsonl"
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

app = FastAPI(title="CamSniff Backend", version="1.0")

INDEX_HTML = """<!DOCTYPE html>
<html lang='en'>
  <head>
    <meta charset='utf-8'/>
    <title>CamSniff Live Events</title>
    <style>
      body { font-family: system-ui, sans-serif; margin: 0; background:#0d1117; color:#e6edf3; }
      header { padding:10px 16px; background:#161b22; position:sticky; top:0; }
      #out { white-space: pre; font-family: ui-monospace, monospace; padding:12px; margin:0; }
      .ok { color:#3fb950; }
      .warn { color:#d29922; }
      .err { color:#f85149; }
      #status { font-size: 0.9em; opacity:0.8 }
    </style>
  </head>
  <body>
    <header>
      <strong>CamSniff Live Events</strong>
      <span id='status'>connecting…</span>
    </header>
    <pre id='out'></pre>
    <script>
      const out = document.getElementById('out');
      const status = document.getElementById('status');
      function fmt(line){
        try { const o = JSON.parse(line); return JSON.stringify(o); } catch { return line; }
      }
      function connect(){
        const ws = new WebSocket((location.protocol === 'https:'?'wss':'ws')+'://'+location.host+'/ws');
        ws.onopen = () => { status.textContent='live'; status.className='ok'; };
        ws.onclose = () => { status.textContent='reconnecting…'; setTimeout(connect, 1500); };
        ws.onmessage = e => { out.textContent += fmt(e.data) + '\n'; if(out.textContent.length>80000){ out.textContent = out.textContent.slice(-60000); } window.scrollTo(0, document.body.scrollHeight); };
      }
      connect();
    </script>
  </body>
</html>"""


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    return INDEX_HTML


@app.get("/health", response_class=PlainTextResponse)
def health() -> str:
    return "ok" if LOG_FILE.exists() else "warming"


def _read_last_lines(path: Path, max_lines: int = 200) -> List[str]:
    """Read at most last max_lines from a potentially large file efficiently."""
    if not path.exists():
        return []
    # Read progressively bigger blocks from end until enough lines
    lines: List[str] = []
    block = 4096
    with path.open("rb") as fh:
        fh.seek(0, os.SEEK_END)
        size = fh.tell()
        data = b""
        while size > 0 and len(lines) <= max_lines:
            read_size = block if size - block > 0 else size
            size -= read_size
            fh.seek(size)
            data = fh.read(read_size) + data
            lines = data.decode(errors="ignore").splitlines()
            block *= 2
    return lines[-max_lines:]


@app.get("/events")
def events(limit: int = Query(100, ge=1, le=1000), level: Optional[str] = None, event: Optional[str] = None):
    """Return last N events; now uses unified logging_utils (event_type field)."""
    results: List[dict] = []
    # iterate in natural order then trim from end for efficiency
    for obj in logging_utils.iter_events(events_path=LOG_FILE):
        if level and obj.get("level") != level:
            continue
        if event and obj.get("event_type") != event:
            continue
        results.append(obj)
    # Return the last 'limit'
    return JSONResponse(results[-limit:])


async def _follow(path: Path) -> AsyncGenerator[str, None]:
    """Async generator yielding new lines appended to file."""
    # Start at current end (stream only new data)
    pos = 0
    while not path.exists():  # wait for file to appear
        await asyncio.sleep(0.5)
    pos = path.stat().st_size
    while True:
        try:
            await asyncio.sleep(0.5)
            if not path.exists():
                continue
            size = path.stat().st_size
            if size < pos:  # rotated/truncated
                pos = 0
            if size == pos:
                continue
            with path.open("r", encoding="utf-8", errors="ignore") as fh:
                fh.seek(pos)
                chunk = fh.read(size - pos)
                pos = size
            for line in chunk.splitlines():
                yield line
        except asyncio.CancelledError:
            break
        except Exception:
            await asyncio.sleep(1)


@app.websocket("/ws")
async def ws_stream(ws: WebSocket):
    await ws.accept()
    # Send a short backlog first
    backlog = _read_last_lines(LOG_FILE, max_lines=40)
    for line in backlog:
        await ws.send_text(line)
    try:
        async for line in _follow(LOG_FILE):
            try:
                json.loads(line)
            except json.JSONDecodeError:
                continue
            await ws.send_text(line)
    except WebSocketDisconnect:
        return
    except Exception:
        await ws.close()


def main():  # entry point callable
    port = int(os.environ.get("CAMSNIFF_BACKEND_PORT", "8089"))
    uvicorn.run(app, host="0.0.0.0", port=port)


if __name__ == "__main__":  # pragma: no cover
    main()
