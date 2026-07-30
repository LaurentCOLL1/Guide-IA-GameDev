from __future__ import annotations
from collections.abc import Hashable, Iterator
from typing import Generic, TypeVar

K = TypeVar("K", bound=Hashable)
V = TypeVar("V")

class StableUniqueList(Generic[K, V]):
    """Insertion-ordered values addressed by a unique stable key."""
    def __init__(self) -> None:
        self._keys: list[K] = []
        self._values: dict[K, V] = {}

    def add(self, key: K, value: V) -> bool:
        if key in self._values:
            return False
        self._keys.append(key)
        self._values[key] = value
        return True

    def replace(self, key: K, value: V) -> bool:
        if key not in self._values:
            return False
        self._values[key] = value
        return True

    def remove(self, key: K) -> bool:
        if key not in self._values:
            return False
        del self._values[key]
        self._keys.remove(key)
        return True

    def contains(self, key: K) -> bool:
        return key in self._values

    def get(self, key: K, default: V | None = None) -> V | None:
        return self._values.get(key, default)

    def values(self) -> list[V]:
        return [self._values[key] for key in self._keys]

    def items(self) -> list[tuple[K, V]]:
        return [(key, self._values[key]) for key in self._keys]

    def __len__(self) -> int:
        return len(self._keys)

    def __iter__(self) -> Iterator[V]:
        return iter(self.values())
