from __future__ import annotations

from dataclasses import dataclass
import time
from typing import Callable, TypeVar

from .cancellation import CancellationToken
from .errors import TransportError

T = TypeVar("T")


@dataclass(frozen=True)
class RetryPolicy:
    max_retries: int = 2
    base_delay_seconds: float = 0.05
    max_delay_seconds: float = 0.5

    def validate(self) -> None:
        if not (0 <= self.max_retries <= 5):
            raise ValueError("max_retries hors limites.")
        if not (0.0 <= self.base_delay_seconds <= self.max_delay_seconds <= 5.0):
            raise ValueError("Délais de reprise invalides.")


class RetryExecutor:
    def __init__(self, policy: RetryPolicy, *, sleep: Callable[[float], None] = time.sleep):
        policy.validate()
        self._policy = policy
        self._sleep = sleep

    def run(self, operation: Callable[[], T], cancellation: CancellationToken) -> T:
        attempt = 0
        while True:
            cancellation.raise_if_cancelled()
            try:
                return operation()
            except TransportError as exc:
                if not exc.retryable or attempt >= self._policy.max_retries:
                    raise
                delay = min(
                    self._policy.max_delay_seconds,
                    self._policy.base_delay_seconds * (2**attempt),
                )
                cancellation.raise_if_cancelled()
                self._sleep(delay)
                attempt += 1
