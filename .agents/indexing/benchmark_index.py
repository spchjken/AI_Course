"""Small repeatable latency probe for the derived-index tools."""

from __future__ import annotations

import argparse
import json
import math
import shutil
import subprocess
import sys
import time
from pathlib import Path


def probe(command: list[str], root: Path, repetitions: int) -> dict[str, object]:
    samples: list[float] = []
    return_codes: list[int] = []
    for _ in range(repetitions):
        started = time.perf_counter()
        result = subprocess.run(command, cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace")
        samples.append(round((time.perf_counter() - started) * 1000, 3))
        return_codes.append(result.returncode)
    ordered = sorted(samples)
    p95 = ordered[max(0, min(len(ordered) - 1, math.ceil(len(ordered) * 0.95) - 1))]
    return {
        "samples_ms": samples,
        "min_ms": min(samples),
        "median_ms": ordered[len(ordered) // 2],
        "p95_ms": p95,
        "max_ms": max(samples),
        "return_codes": return_codes,
        "pass": all(code == 0 for code in return_codes),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--repetitions", type=int, default=5)
    args = parser.parse_args(argv)
    root = args.root.resolve()
    tool = root / ".agents/indexing/sync_index.py"
    search_tool = root / ".agents/indexing/search_index.py"
    python = sys.executable
    repetitions = max(2, args.repetitions)
    # Establish a current baseline before timing no-op and query paths.
    full = probe([python, "-B", str(tool), "--full"], root, 1)
    report = {
        "tool_version": "0.1",
        "root": str(root),
        "rg_available": shutil.which("rg") is not None,
        "full_rebuild": full,
        "no_op_check": probe([python, "-B", str(tool), "--check"], root, repetitions),
        "incremental_update": probe([python, "-B", str(tool), "--update"], root, repetitions),
        "lexical_search": probe([python, "-B", str(search_tool), "quality gate"], root, repetitions),
        "targets_ms": {"full_rebuild": 10000, "no_op_check": 750, "incremental_update": 1000, "lexical_search": 1000},
    }
    for name, target in report["targets_ms"].items():
        result = report[name]
        result["target_ms"] = target
        result["within_target"] = bool(result["pass"] and result["p95_ms"] <= target)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if all(report[name]["within_target"] for name in report["targets_ms"]) else 2


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
