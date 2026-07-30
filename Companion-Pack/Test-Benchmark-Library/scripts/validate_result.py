#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PACK_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACK_ROOT / "python" / "src"))
from benchmark_library.formats import read_json
from benchmark_library.validation import validate_result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("results", nargs="+", type=Path)
    args = parser.parse_args()
    failures = {}
    for path in args.results:
        errors = validate_result(read_json(path))
        if errors:
            failures[str(path)] = errors
    print(json.dumps({"status":"success" if not failures else "failure","files":len(args.results),"failures":failures}, sort_keys=True))
    return 1 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
