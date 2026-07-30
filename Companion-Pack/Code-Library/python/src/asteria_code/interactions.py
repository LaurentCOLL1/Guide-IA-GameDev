from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True, slots=True)
class InteractionResult:
    ok: bool
    value: Any = None
    error_code: str = ""

Handler = Callable[[Any], Any]

class InteractionRouter:
    def __init__(self) -> None:
        self._handlers: dict[str, Handler] = {}

    def register(self, action: str, handler: Handler, *, replace: bool = False) -> None:
        if not action:
            raise ValueError("action must not be empty")
        if action in self._handlers and not replace:
            raise KeyError(f"Handler already registered: {action}")
        self._handlers[action] = handler

    def contains(self, action: str) -> bool:
        return action in self._handlers

    def dispatch(self, action: str, context: Any = None) -> InteractionResult:
        handler = self._handlers.get(action)
        if handler is None:
            return InteractionResult(False, error_code="unknown_action")
        try:
            return InteractionResult(True, value=handler(context))
        except Exception as exc:
            return InteractionResult(False, error_code=f"handler_error:{type(exc).__name__}")
