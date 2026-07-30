from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

class ManualClock:
    def __init__(self, initial_seconds: float = 0.0) -> None:
        if initial_seconds < 0:
            raise ValueError("initial_seconds must be non-negative")
        self._seconds = float(initial_seconds)

    def now(self) -> float:
        return self._seconds

    def advance(self, seconds: float) -> float:
        if seconds < 0:
            raise ValueError("seconds must be non-negative")
        self._seconds += seconds
        return self._seconds

@dataclass(slots=True)
class EventRecorder:
    events: list[tuple[str, Any]] = field(default_factory=list)

    def record(self, name: str, payload: Any = None) -> None:
        self.events.append((name, payload))

    def count(self, name: str | None = None) -> int:
        if name is None:
            return len(self.events)
        return sum(1 for event_name, _ in self.events if event_name == name)

    def last(self, name: str | None = None) -> tuple[str, Any] | None:
        if name is None:
            return self.events[-1] if self.events else None
        for event in reversed(self.events):
            if event[0] == name:
                return event
        return None
