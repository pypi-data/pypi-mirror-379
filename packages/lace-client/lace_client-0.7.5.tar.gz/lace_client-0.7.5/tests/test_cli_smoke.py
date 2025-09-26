import os
import subprocess
import sys
from pathlib import Path


def test_dry_run():
    repo = Path(__file__).resolve().parents[1]
    env = os.environ.copy()
    env["PYTHONPATH"] = str(repo / "src")
    cmd = [
        sys.executable,
        "-m",
        "lace.cli",
        "pack",
        str(repo / "examples" / "sample"),
        "--answers-file",
        str(repo / "examples" / "answers_sample.json"),
        "--dry-run",
    ]
    cp = subprocess.run(cmd, env=env, capture_output=True, text=True)
    assert cp.returncode == 0, cp.stderr
    out = cp.stdout + cp.stderr
    assert "Dry-run" in out or "Dry-run mode" in out
