from __future__ import annotations

from collections import OrderedDict
from dataclasses import dataclass
import time
from typing import Callable, Generic, TypeVar

T = TypeVar("T")


@dataclass
class _Entry(Generic[T]):
    value: T
    expires_at: float


class TTLCache(Generic[T]):
    def __init__(
        self,
        *,
        max_entries: int = 128,
        ttl_seconds: float = 30.0,
        clock: Callable[[], float] = time.monotonic,
    ):
        if max_entries < 1 or max_entries > 4096:
            raise ValueError("max_entries hors limites.")
        if ttl_seconds < 0.0 or ttl_seconds > 3600.0:
            raise ValueError("ttl_seconds hors limites.")
        self._max_entries = max_entries
        self._ttl_seconds = ttl_seconds
        self._clock = clock
        self._entries: OrderedDict[str, _Entry[T]] = OrderedDict()

    def get(self, key: str) -> T | None:
        entry = self._entries.get(key)
        if entry is None:
            return None
        if entry.expires_at <= self._clock():
            del self._entries[key]
            return None
        self._entries.move_to_end(key)
        return entry.value

    def put(self, key: str, value: T) -> None:
        if self._ttl_seconds == 0.0:
            return
        self._entries[key] = _Entry(value=value, expires_at=self._clock() + self._ttl_seconds)
        self._entries.move_to_end(key)
        while len(self._entries) > self._max_entries:
            self._entries.popitem(last=False)

    def clear(self) -> None:
        self._entries.clear()

    def __len__(self) -> int:
        return len(self._entries)
