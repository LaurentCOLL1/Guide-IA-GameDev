from __future__ import annotations

import re
from typing import Mapping

from .contracts import AiRequest
from .errors import SafetyError

_BEARER = re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/=-]{8,}")
_KEY_VALUE = re.compile(r"(?i)\b(api[_-]?key|token|secret)\s*[:=]\s*[^\s,;]{4,}")


class SafetyPolicy:
    def __init__(
        self,
        *,
        allowed_operations: set[str] | None = None,
        max_total_prompt_chars: int = 32_000,
    ):
        self.allowed_operations = allowed_operations or {
            "chat.completions",
            "models.list",
            "embeddings.create",
        }
        self.max_total_prompt_chars = max_total_prompt_chars

    def validate_request(self, request: AiRequest) -> None:
        request.validate()
        if request.operation not in self.allowed_operations:
            raise SafetyError("Opération refusée par la politique.")
        total = 0
        for message in request.messages:
            total += len(message.content)
            for char in message.content:
                if ord(char) < 32 and char not in {"\n", "\t"}:
                    raise SafetyError("Caractère de contrôle refusé.")
        if total > self.max_total_prompt_chars:
            raise SafetyError("Payload textuel trop volumineux.")

    @staticmethod
    def redact_text(value: str) -> str:
        value = _BEARER.sub("Bearer [REDACTED]", value)
        return _KEY_VALUE.sub(lambda match: f"{match.group(1)}=[REDACTED]", value)

    @staticmethod
    def redact_headers(headers: Mapping[str, str]) -> dict[str, str]:
        result: dict[str, str] = {}
        for key, value in headers.items():
            if key.lower() in {"authorization", "proxy-authorization", "x-api-key"}:
                result[key] = "[REDACTED]"
            else:
                result[key] = SafetyPolicy.redact_text(value)
        return result
