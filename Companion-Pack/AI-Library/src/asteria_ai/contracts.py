from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterable

from .errors import ProtocolError

_ALLOWED_ROLES = {"system", "user", "assistant"}


@dataclass(frozen=True)
class AiMessage:
    role: str
    content: str

    def validate(self) -> None:
        if self.role not in _ALLOWED_ROLES:
            raise ProtocolError(f"Rôle non autorisé: {self.role!r}")
        if not isinstance(self.content, str) or not self.content:
            raise ProtocolError("Le contenu du message doit être une chaîne non vide.")


@dataclass(frozen=True)
class AiRequest:
    request_id: str
    operation: str
    model: str
    messages: tuple[AiMessage, ...]
    timeout_ms: int = 15_000
    max_output_tokens: int = 256
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def chat(
        cls,
        *,
        request_id: str,
        model: str,
        messages: Iterable[AiMessage],
        timeout_ms: int = 15_000,
        max_output_tokens: int = 256,
        metadata: dict[str, Any] | None = None,
    ) -> "AiRequest":
        return cls(
            request_id=request_id,
            operation="chat.completions",
            model=model,
            messages=tuple(messages),
            timeout_ms=timeout_ms,
            max_output_tokens=max_output_tokens,
            metadata=dict(metadata or {}),
        )

    def validate(self) -> None:
        if not self.request_id or len(self.request_id) > 128:
            raise ProtocolError("request_id absent ou trop long.")
        if self.operation not in {"chat.completions", "models.list", "embeddings.create"}:
            raise ProtocolError(f"Opération non autorisée: {self.operation!r}")
        if not self.model or len(self.model) > 256:
            raise ProtocolError("model absent ou trop long.")
        if self.timeout_ms < 100 or self.timeout_ms > 120_000:
            raise ProtocolError("timeout_ms hors limites.")
        if self.max_output_tokens < 1 or self.max_output_tokens > 32_768:
            raise ProtocolError("max_output_tokens hors limites.")
        if len(self.messages) > 64:
            raise ProtocolError("Trop de messages.")
        for message in self.messages:
            message.validate()


@dataclass(frozen=True)
class AiError:
    code: str
    message: str
    retryable: bool = False
    status_code: int | None = None


@dataclass(frozen=True)
class AiResponse:
    request_id: str
    provider: str
    model: str
    text: str
    finish_reason: str
    usage: dict[str, int] = field(default_factory=dict)
    raw_metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        if not self.request_id:
            raise ProtocolError("Réponse sans request_id.")
        if not self.provider:
            raise ProtocolError("Réponse sans fournisseur.")
        if not isinstance(self.text, str):
            raise ProtocolError("Réponse textuelle invalide.")
