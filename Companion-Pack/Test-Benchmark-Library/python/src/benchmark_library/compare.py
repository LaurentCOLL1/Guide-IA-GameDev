from __future__ import annotations

from typing import Any


def compare_results(baseline: dict[str, Any], candidate: dict[str, Any]) -> dict[str, Any]:
    reasons: list[str] = []
    for field in ("benchmark_id", "contract_version", "implementation", "metric", "unit", "seed", "parameters"):
        if baseline.get(field) != candidate.get(field):
            reasons.append(f"different-{field}")
    if baseline.get("environment", {}).get("environment_id") != candidate.get("environment", {}).get("environment_id"):
        reasons.append("different-environment")
    if reasons:
        return {"schema_version": 1, "status": "not-comparable", "baseline": baseline.get("benchmark_id"), "candidate": candidate.get("benchmark_id"), "reasons": reasons, "decision": "repeat under one compatible protocol"}
    base = float(baseline["statistics"]["median"])
    cand = float(candidate["statistics"]["median"])
    delta = cand - base
    delta_pct = (delta / base * 100.0) if base else 0.0
    return {"schema_version": 1, "status": "comparable", "baseline": baseline["benchmark_id"], "candidate": candidate["benchmark_id"], "reasons": [], "baseline_median": base, "candidate_median": cand, "delta": delta, "delta_pct": delta_pct, "decision": "numerical delta only; practical decision requires a predeclared threshold"}
