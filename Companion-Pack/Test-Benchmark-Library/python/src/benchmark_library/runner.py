from __future__ import annotations

import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

from .environment import safe_environment
from .stats import summarize
from .workloads import cpu_workload, memory_workload, corpus_workload


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _measure(benchmark_id: str, unit: str, warmups: int, repetitions: int, operation: Callable[[], tuple[str, dict[str, float]]]) -> tuple[list[dict[str, Any]], str, dict[str, float]]:
    if repetitions < 2:
        raise ValueError("repetitions must be at least 2")
    expected_checksum: str | None = None
    for _ in range(warmups):
        checksum, _ = operation()
        expected_checksum = expected_checksum or checksum
        if checksum != expected_checksum:
            raise RuntimeError("warm-up checksum changed")
    samples: list[dict[str, Any]] = []
    secondary_totals: dict[str, list[float]] = {}
    for index in range(repetitions):
        started = time.perf_counter_ns()
        checksum, secondary = operation()
        elapsed = time.perf_counter_ns() - started
        expected_checksum = expected_checksum or checksum
        status = "pass" if checksum == expected_checksum else "fail"
        sample: dict[str, Any] = {"benchmark_id": benchmark_id, "sample_index": index, "value": elapsed, "unit": unit, "status": status, "checksum": checksum}
        if secondary:
            key, value = next(iter(secondary.items()))
            sample["secondary_value"] = value
            sample["secondary_unit"] = key
            secondary_totals.setdefault(key, []).append(float(value))
        samples.append(sample)
    if any(sample["status"] != "pass" for sample in samples):
        raise RuntimeError("oracle failed")
    secondary_summary = {key: summarize(values) for key, values in secondary_totals.items()}
    return samples, expected_checksum or "", secondary_summary


def run_benchmark(kind: str, contract: dict[str, Any], pack_root: Path, environment_extra: dict[str, Any] | None = None) -> dict[str, Any]:
    parameters = contract["parameters"]
    seed = int(contract["seed"])
    if kind == "cpu":
        operation = lambda: (cpu_workload(seed, int(parameters["iterations"]), int(parameters["payload_bytes"])), {})
    elif kind == "memory":
        def operation() -> tuple[str, dict[str, float]]:
            checksum, peak = memory_workload(seed, int(parameters["items"]))
            return str(checksum), {"peak_bytes": float(peak)}
    elif kind == "corpus":
        corpus_dir = pack_root / "fixtures" / "corpus"
        def operation() -> tuple[str, dict[str, float]]:
            checksum, accuracy = corpus_workload(corpus_dir / "synthetic-documents.jsonl", corpus_dir / "synthetic-queries.jsonl", int(parameters["queries"]))
            return checksum, {"accuracy": accuracy}
    else:
        raise ValueError(f"unknown benchmark: {kind}")
    samples, checksum, secondary = _measure(contract["id"], contract["unit"], int(contract["warmups"]), int(contract["repetitions"]), operation)
    values = [float(sample["value"]) for sample in samples]
    return {
        "schema_version": 1,
        "benchmark_id": contract["id"],
        "contract_version": contract["version"],
        "family": contract["family"],
        "implementation": contract["implementation"],
        "generated_at_utc": utc_now(),
        "environment": safe_environment(environment_extra),
        "seed": seed,
        "parameters": parameters,
        "warmups": contract["warmups"],
        "repetitions": contract["repetitions"],
        "metric": contract["metric"],
        "unit": contract["unit"],
        "samples": samples,
        "statistics": summarize(values),
        "secondary_statistics": secondary,
        "oracle_status": "pass",
        "oracle_checksum": checksum,
        "evidence_level": "local-measurement",
        "comparability": "same-environment-only",
        "reservations": ["synthetic workload", "no universal performance claim", "same contract and environment required for comparison"],
    }
