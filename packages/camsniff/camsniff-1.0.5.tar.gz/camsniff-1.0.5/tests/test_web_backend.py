import os
import json
from pathlib import Path
from fastapi.testclient import TestClient

# Adjust import path if running via pytest from repo root
from python_core.web_backend import app, LOG_FILE  # type: ignore

client = TestClient(app)


def ensure_log():
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not LOG_FILE.exists():
        LOG_FILE.write_text('{"ts":"2025-01-01T00:00:00Z","level":"info","event_type":"boot","msg":"init"}\n')


def test_health():
    ensure_log()
    r = client.get("/health")
    assert r.status_code == 200
    assert r.text in {"ok", "warming"}


def test_events_endpoint():
    ensure_log()
    # append a second line
    with LOG_FILE.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps({"ts": "2025-01-01T00:00:01Z", "level": "event", "event_type": "camera_found", "ip": "1.2.3.4"}) + "\n")
    r = client.get("/events?limit=5")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    # ensure we at least see one object with expected keys
    assert any("event_type" in o for o in data)


def test_index_html():
    r = client.get("/")
    assert r.status_code == 200
    assert "CamSniff Live Events" in r.text
