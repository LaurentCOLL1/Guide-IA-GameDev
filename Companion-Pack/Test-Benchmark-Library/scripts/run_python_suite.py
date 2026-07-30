#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PACK_ROOT = Path(__file__).resolve().parents[1]
SRC = PACK_ROOT / "python" / "src"
sys.path.insert(0, str(SRC))

from benchmark_library.formats import write_json, write_samples_csv
from benchmark_library.runner import run_benchmark

CONTRACTS = {
    "cpu": "CPU-REFERENCE.json",
    "memory": "MEMORY-REFERENCE.json",
    "corpus": "CORPUS-REFERENCE.json",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--benchmark", choices=["cpu", "memory", "corpus", "all"], required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--repetitions", type=int)
    parser.add_argument("--warmups", type=int)
    parser.add_argument("--iterations", type=int)
    parser.add_argument("--items", type=int)
    parser.add_argument("--queries", type=int)
    args = parser.parse_args()
    selected = list(CONTRACTS) if args.benchmark == "all" else [args.benchmark]
    args.output_dir.mkdir(parents=True, exist_ok=True)
    generated = []
    for kind in selected:
        contract = json.loads((PACK_ROOT / "contracts" / CONTRACTS[kind]).read_text(encoding="utf-8"))
        if args.repetitions is not None:
            contract["repetitions"] = args.repetitions
        if args.warmups is not None:
            contract["warmups"] = args.warmups
        if kind == "cpu" and args.iterations is not None:
            contract["parameters"]["iterations"] = args.iterations
        if kind == "memory" and args.items is not None:
            contract["parameters"]["items"] = args.items
        if kind == "corpus" and args.queries is not None:
            contract["parameters"]["queries"] = args.queries
        result = run_benchmark(kind, contract, PACK_ROOT)
        write_json(args.output_dir / f"{kind}-summary.json", result)
        write_samples_csv(args.output_dir / f"{kind}-samples.csv", result["samples"])
        generated.extend([f"{kind}-summary.json", f"{kind}-samples.csv"])
    write_json(args.output_dir / "suite-manifest.yaml", {"schema_version":1,"status":"success","generated":generated,"note":"JSON syntax is valid YAML 1.2"})
    print(json.dumps({"status":"success","benchmarks":selected,"generated":generated}, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
