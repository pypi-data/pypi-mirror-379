from python_core import config

def test_output_root_created(tmp_path, monkeypatch):
    monkeypatch.setenv("CAMSNIFF_OUTPUT", str(tmp_path / "outdir"))
    root = config.output_root()
    assert root.exists()
    assert root.name == "outdir"


def test_paths():
    logs = config.logs_dir()
    assert logs.exists()
    scan = config.scan_log_file()
    assert scan.parent == logs
    # db path doesn't have to exist yet
    assert config.db_path().name == "results.sqlite"
