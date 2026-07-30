from __future__ import annotations

from dataclasses import dataclass, field
import heapq
import itertools
from typing import Any

from .errors import QueueFullError


@dataclass(order=True)
class QueuedTask:
    priority: int
    sequence: int
    task_id: str = field(compare=False)
    payload: Any = field(compare=False)
    cancelled: bool = field(default=False, compare=False)


class BoundedTaskQueue:
    def __init__(self, max_size: int = 8):
        if max_size < 1 or max_size > 1024:
            raise ValueError("max_size hors limites.")
        self._max_size = max_size
        self._heap: list[QueuedTask] = []
        self._tasks: dict[str, QueuedTask] = {}
        self._sequence = itertools.count()

    def submit(self, task_id: str, payload: Any, *, priority: int = 100) -> None:
        if not task_id or task_id in self._tasks:
            raise ValueError("task_id absent ou dupliqué.")
        if len(self._tasks) >= self._max_size:
            raise QueueFullError("File IA saturée.")
        task = QueuedTask(priority, next(self._sequence), task_id, payload)
        self._tasks[task_id] = task
        heapq.heappush(self._heap, task)

    def cancel(self, task_id: str) -> bool:
        task = self._tasks.get(task_id)
        if task is None:
            return False
        task.cancelled = True
        return True

    def pop(self) -> QueuedTask | None:
        while self._heap:
            task = heapq.heappop(self._heap)
            self._tasks.pop(task.task_id, None)
            if not task.cancelled:
                return task
        return None

    def __len__(self) -> int:
        return len(self._tasks)
