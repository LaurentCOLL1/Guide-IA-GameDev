from __future__ import annotations

import hashlib
import json
import os
import platform
from pathlib import Path
from typing import Any


def _read_first(path: str, prefix: str | None = None) -> str:
    try:
        for line in Path(path).read_text(encoding="utf-8", errors="replace").splitlines():
            if prefix is None or line.startswith(prefix):
                return line.split(":", 1)[-1].strip()
    except OSError:
        pass
    return "unknown"


def safe_environment(extra: dict[str, Any] | None = None) -> dict[str, Any]:
    memory_kib = _read_first("/proc/meminfo", "MemTotal")
    cpu_model = _read_first("/proc/cpuinfo", "model name")
    data: dict[str, Any] = {
        "os": platform.system(),
        "os_release": platform.release(),
        "architecture": platform.machine(),
        "runtime": f"{platform.python_implementation()} {platform.python_version()}",
        "cpu_model": cpu_model or platform.processor() or "unknown",
        "logical_cpu_count": os.cpu_count() or 1,
        "memory_total": memory_kib,
        "virtualization_hint": os.environ.get("RUNNER_ENVIRONMENT", "unknown"),
        "runner_image": os.environ.get("ImageOS", "unknown"),
    }
    if extra:
        data.update(extra)
    forbidden = ("hostname", "user", "username", "home", "ip", "secret", "token")
    for key in data:
        if any(word in key.lower() for word in forbidden):
            raise ValueError(f"unsafe environment field: {key}")
    canonical = json.dumps(data, ensure_ascii=True, sort_keys=True, separators=(",", ":"))
    data["environment_id"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return data
