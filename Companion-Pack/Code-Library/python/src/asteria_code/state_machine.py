from __future__ import annotations
from dataclasses import dataclass
from typing import Hashable, TypeVar

S = TypeVar("S", bound=Hashable)
E = TypeVar("E", bound=Hashable)

@dataclass(frozen=True, slots=True)
class Transition:
    source: S
    event: E
    target: S

class StateMachine:
    def __init__(self, initial_state: S) -> None:
        self._state = initial_state
        self._transitions: dict[tuple[S, E], S] = {}

    @property
    def current_state(self) -> S:
        return self._state

    def add_transition(self, source: S, event: E, target: S, *, replace: bool = False) -> None:
        key = (source, event)
        if key in self._transitions and not replace:
            raise KeyError(f"Transition already exists: {source!r}/{event!r}")
        self._transitions[key] = target

    def can_trigger(self, event: E) -> bool:
        return (self._state, event) in self._transitions

    def trigger(self, event: E) -> Transition | None:
        key = (self._state, event)
        target = self._transitions.get(key)
        if target is None:
            return None
        transition = Transition(self._state, event, target)
        self._state = target
        return transition
