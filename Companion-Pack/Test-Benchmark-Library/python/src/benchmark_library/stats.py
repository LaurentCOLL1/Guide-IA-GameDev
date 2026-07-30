from __future__ import annotations

import math
import statistics
from typing import Iterable


def percentile(values: Iterable[float], quantile: float) -> float:
    data = sorted(float(v) for v in values)
    if not data:
        raise ValueError("values must not be empty")
    if not 0.0 <= quantile <= 1.0:
        raise ValueError("quantile must be between 0 and 1")
    if len(data) == 1:
        return data[0]
    position = (len(data) - 1) * quantile
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return data[lower]
    fraction = position - lower
    return data[lower] + (data[upper] - data[lower]) * fraction


def summarize(values: Iterable[float]) -> dict[str, float | int]:
    data = [float(v) for v in values]
    if not data:
        raise ValueError("values must not be empty")
    mean = statistics.fmean(data)
    variance = statistics.variance(data) if len(data) > 1 else 0.0
    stdev = math.sqrt(variance)
    return {
        "count": len(data),
        "min": min(data),
        "max": max(data),
        "mean": mean,
        "median": statistics.median(data),
        "variance": variance,
        "stdev": stdev,
        "coefficient_of_variation": stdev / mean if mean else 0.0,
        "p95": percentile(data, 0.95),
        "p99": percentile(data, 0.99),
    }
