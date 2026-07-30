from __future__ import annotations

from datetime import datetime
from typing import Any

FORBIDDEN_ENV_KEYS = ("hostname", "username", "user", "home", "ip", "secret", "token")


def validate_result(result: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = ["benchmark_id", "contract_version", "generated_at_utc", "environment", "samples", "statistics", "oracle_status", "comparability"]
    for field in required:
        if field not in result:
            errors.append(f"missing:{field}")
    try:
        datetime.fromisoformat(str(result.get("generated_at_utc", "")).replace("Z", "+00:00"))
    except ValueError:
        errors.append("invalid:generated_at_utc")
    samples = result.get("samples", [])
    if len(samples) < 2:
        errors.append("samples:minimum-2")
    if any(sample.get("status") != "pass" for sample in samples):
        errors.append("samples:oracle-failure")
    stats = result.get("statistics", {})
    for field in ("count", "mean", "median", "variance", "stdev", "coefficient_of_variation", "p95", "p99"):
        if field not in stats:
            errors.append(f"statistics:missing-{field}")
    environment = result.get("environment", {})
    if len(str(environment.get("environment_id", ""))) != 64:
        errors.append("environment:invalid-id")
    for key in environment:
        if any(word in key.lower() for word in FORBIDDEN_ENV_KEYS):
            errors.append(f"environment:unsafe-{key}")
    if result.get("oracle_status") != "pass":
        errors.append("oracle:not-pass")
    return errors
