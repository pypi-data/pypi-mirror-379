import json
from lace.client import LaceClient


def test_analyze_payload_strips_absolute_paths(tmp_path):
    client = LaceClient(api_key="test")
    payload = {
        "manifest": {
            "total_files": 1,
            "total_bytes": 10,
            "files": [
                {
                    "hash": "a" * 64,
                    "path": str(tmp_path / "secret/abs/path/file.txt"),
                    "relpath": "file.txt",
                    "size": 10,
                    "mtime": 1_600_000_000,
                }
            ],
        },
        "config": {},
    }

    normalized = client._normalize_analyze_payload_for_server(payload)
    files = normalized["manifest"]["files"]
    assert "path" not in files[0]  # absolute path must not be present
    assert files[0]["relpath"] == "file.txt"
    assert files[0]["hash"] == "a" * 64
    # mtime converted to ISO8601
    assert files[0]["mtime"].endswith("Z")
