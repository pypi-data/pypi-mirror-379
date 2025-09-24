import json
from pathlib import Path

from python_core import logging_utils


def test_emit_and_iter_events(tmp_path):
    log_file = tmp_path / "scan.jsonl"
    # emit three events with different types and a payload
    logging_utils.emit_event("camera_found", payload={"ip": "1.2.3.4"}, events_path=log_file)
    logging_utils.emit_event("scan_start", category="scan", events_path=log_file)
    logging_utils.emit_event("camera_found", payload={"ip": "5.6.7.8"}, events_path=log_file)

    # basic iteration
    events = list(logging_utils.iter_events(events_path=log_file))
    assert len(events) == 3
    assert events[0]["event_type"] == "camera_found"

    # filter by type
    cam_events = list(logging_utils.iter_events(events_path=log_file, event_types=["camera_found"]))
    assert len(cam_events) == 2
    assert all(e["event_type"] == "camera_found" for e in cam_events)

    # since_ts (use the ts of second event, expect only third)
    since = events[1]["ts"]
    later = list(logging_utils.iter_events(events_path=log_file, since_ts=since))
    assert len(later) == 1
    assert later[0]["payload"]["ip"] == "5.6.7.8"


def test_tail_events_once(tmp_path):
    log_file = tmp_path / "scan.jsonl"
    # Write some malformed + valid lines
    # Include one malformed line (not-json) and one empty JSON object
    log_file.write_text("not-json\n{}\n", encoding="utf-8")
    logging_utils.emit_event("boot", events_path=log_file)

    events = list(logging_utils.tail_events(events_path=log_file, follow=False))
    # Should skip malformed, include empty JSON object and boot event
    assert len(events) == 2
    assert events[-1]["event_type"] == "boot"
