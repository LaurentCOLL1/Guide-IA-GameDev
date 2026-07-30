from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import os
from urllib.parse import urlparse

from .errors import ConfigurationError


class ProviderKind(str, Enum):
    OLLAMA = "ollama"
    LLAMA_CPP = "llama_cpp"
    LOCALAI = "localai"


_DEFAULT_URLS = {
    ProviderKind.OLLAMA: "http://127.0.0.1:11434",
    ProviderKind.LLAMA_CPP: "http://127.0.0.1:8080",
    ProviderKind.LOCALAI: "http://127.0.0.1:8080",
}


@dataclass(frozen=True)
class AiClientConfig:
    provider: ProviderKind
    base_url: str
    websocket_url: str | None = None
    api_key_env: str | None = None
    connect_timeout_seconds: float = 2.0
    request_timeout_seconds: float = 15.0
    max_response_bytes: int = 4 * 1024 * 1024
    max_in_flight: int = 8
    max_retries: int = 2
    cache_ttl_seconds: float = 30.0
    allow_remote: bool = False

    @classmethod
    def for_provider(
        cls,
        provider: ProviderKind,
        *,
        base_url: str | None = None,
        websocket_url: str | None = None,
        api_key_env: str | None = None,
        **overrides,
    ) -> "AiClientConfig":
        config = cls(
            provider=provider,
            base_url=(base_url or _DEFAULT_URLS[provider]).rstrip("/"),
            websocket_url=websocket_url,
            api_key_env=api_key_env,
            **overrides,
        )
        config.validate()
        return config

    def validate(self) -> None:
        parsed = urlparse(self.base_url)
        if parsed.scheme not in {"http", "https"}:
            raise ConfigurationError("base_url doit utiliser http ou https.")
        if parsed.username or parsed.password:
            raise ConfigurationError("Les identifiants ne doivent pas être placés dans l’URL.")
        if not parsed.hostname or parsed.port is None:
            raise ConfigurationError("base_url doit inclure un hôte et un port.")
        if parsed.path not in {"", "/"} or parsed.query or parsed.fragment:
            raise ConfigurationError("base_url doit désigner la racine du service.")
        if not self.allow_remote and parsed.hostname not in {"127.0.0.1", "::1", "localhost"}:
            raise ConfigurationError("Un hôte distant est refusé par défaut.")
        if self.allow_remote and parsed.scheme != "https":
            raise ConfigurationError("Un hôte distant exige https.")
        if self.websocket_url is not None:
            ws = urlparse(self.websocket_url)
            if ws.scheme not in {"ws", "wss"} or not ws.hostname or ws.port is None:
                raise ConfigurationError("websocket_url invalide.")
            if not self.allow_remote and ws.hostname not in {"127.0.0.1", "::1", "localhost"}:
                raise ConfigurationError("Un WebSocket distant est refusé par défaut.")
            if self.allow_remote and ws.scheme != "wss":
                raise ConfigurationError("Un WebSocket distant exige wss.")
        if not (0.1 <= self.connect_timeout_seconds <= 30.0):
            raise ConfigurationError("connect_timeout_seconds hors limites.")
        if not (0.1 <= self.request_timeout_seconds <= 120.0):
            raise ConfigurationError("request_timeout_seconds hors limites.")
        if not (1024 <= self.max_response_bytes <= 32 * 1024 * 1024):
            raise ConfigurationError("max_response_bytes hors limites.")
        if not (1 <= self.max_in_flight <= 64):
            raise ConfigurationError("max_in_flight hors limites.")
        if not (0 <= self.max_retries <= 5):
            raise ConfigurationError("max_retries hors limites.")
        if not (0.0 <= self.cache_ttl_seconds <= 3600.0):
            raise ConfigurationError("cache_ttl_seconds hors limites.")
        if self.api_key_env is not None and not self.api_key_env.replace("_", "").isalnum():
            raise ConfigurationError("api_key_env doit être un nom de variable simple.")

    def api_key(self) -> str | None:
        if self.api_key_env is None:
            return None
        value = os.environ.get(self.api_key_env)
        return value if value else None
