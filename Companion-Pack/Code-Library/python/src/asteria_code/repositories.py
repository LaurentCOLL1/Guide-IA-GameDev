from __future__ import annotations
import copy
from collections.abc import Hashable
from typing import Generic, TypeVar

K = TypeVar("K", bound=Hashable)
V = TypeVar("V")

class InMemoryRepository(Generic[K, V]):
    """Small deterministic repository with defensive copies."""
    def __init__(self) -> None:
        self._rows: dict[K, V] = {}

    def save(self, entity_id: K, entity: V) -> None:
        self._rows[entity_id] = copy.deepcopy(entity)

    def get_by_id(self, entity_id: K) -> V | None:
        entity = self._rows.get(entity_id)
        return copy.deepcopy(entity) if entity is not None else None

    def contains(self, entity_id: K) -> bool:
        return entity_id in self._rows

    def remove(self, entity_id: K) -> bool:
        return self._rows.pop(entity_id, None) is not None

    def list_ids(self) -> list[K]:
        return sorted(self._rows, key=lambda item: str(item))

    def clear(self) -> None:
        self._rows.clear()

    def count(self) -> int:
        return len(self._rows)
