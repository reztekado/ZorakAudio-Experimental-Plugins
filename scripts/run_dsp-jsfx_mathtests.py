#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, capture_output=True)


def expect_ok(cmd: list[str], label: str) -> None:
    cp = run(cmd)
    if cp.returncode != 0:
        print(f"[FAIL] {label}")
        print(cp.stdout)
        print(cp.stderr)
        raise SystemExit(1)
    print(f"[ OK ] {label}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=str(Path(__file__).resolve().parents[1]))
    args = ap.parse_args()

    repo_root = Path(args.repo_root).resolve()
    aot = repo_root / "dsp_jsfx_aot.py"
    tests = repo_root / "tests" / "dsp-jsfx-math"
    out = repo_root / "build" / "mathtests"
    out.mkdir(parents=True, exist_ok=True)

    stem = "math_builtins_all"
    expect_ok([
        sys.executable,
        str(aot),
        str(tests / f"{stem}.jsfx"),
        "--out-ll", str(out / f"{stem}.ll"),
        "--out-h", str(out / f"{stem}.h"),
        "--meta", str(out / f"{stem}.json"),
        "--out-obj", str(out / f"{stem}.o"),
    ], "all documented simple math builtins compile")
