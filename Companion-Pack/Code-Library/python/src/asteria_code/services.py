from __future__ import annotations
from typing import Any, TypeVar

T = TypeVar("T")

class ServiceRegistry:
    """Explicit service registry; intentionally not a global singleton."""
    def __init__(self) -> None:
        self._services: dict[str, Any] = {}

    def register(self, service_id: str, service: Any, *, replace: bool = False) -> None:
        if not service_id:
            raise ValueError("service_id must not be empty")
        if service_id in self._services and not replace:
            raise KeyError(f"Service already registered: {service_id}")
        self._services[service_id] = service

    def resolve(self, service_id: str, expected_type: type[T] | None = None) -> T | Any:
        if service_id not in self._services:
            raise KeyError(f"Unknown service: {service_id}")
        service = self._services[service_id]
        if expected_type is not None and not isinstance(service, expected_type):
            raise TypeError(f"Service {service_id} is not {expected_type.__name__}")
        return service

    def contains(self, service_id: str) -> bool:
        return service_id in self._services

    def remove(self, service_id: str) -> bool:
        return self._services.pop(service_id, None) is not None

    def ids(self) -> list[str]:
        return sorted(self._services)
