from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path


def utc_now_text() -> str:
    """Return an RFC 3339 UTC timestamp with an explicit Z suffix."""
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def pack_root() -> Path:
    """Return the Database Library pack root from the installed source layout."""
    return Path(__file__).resolve().parents[3]
