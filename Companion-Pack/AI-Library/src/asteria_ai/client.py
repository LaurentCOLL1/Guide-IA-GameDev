from __future__ import annotations

import hashlib
import json

from .cache import TTLCache
from .cancellation import CancellationToken
from .config import AiClientConfig
from .contracts import AiRequest, AiResponse
from .errors import TransportError
from .providers import adapter
from .retry import RetryExecutor, RetryPolicy
from .safety import SafetyPolicy
from .transports import HttpJsonTransport


class AiClient:
    def __init__(
        self,
        config: AiClientConfig,
        *,
        transport: HttpJsonTransport | None = None,
        safety: SafetyPolicy | None = None,
    ):
        config.validate()
        self._config = config
        self._adapter = adapter(config.provider)
        self._transport = transport or HttpJsonTransport()
        self._safety = safety or SafetyPolicy()
        self._cache: TTLCache[AiResponse] = TTLCache(
            max_entries=128, ttl_seconds=config.cache_ttl_seconds
        )
        self._retry = RetryExecutor(
            RetryPolicy(max_retries=config.max_retries)
        )

    def chat(
        self,
        request: AiRequest,
        cancellation: CancellationToken | None = None,
    ) -> AiResponse:
        token = cancellation or CancellationToken()
        self._safety.validate_request(request)
        key = self._cache_key(request)
        cached = self._cache.get(key)
        if cached is not None:
            return cached

        def perform() -> AiResponse:
            token.raise_if_cancelled()
            payload = self._adapter.encode_chat(request)
            headers = {"X-Asteria-Request-Id": request.request_id}
            api_key = self._config.api_key()
            if api_key:
                headers["Authorization"] = f"Bearer {api_key}"
            result = self._transport.post_json(
                url=self._config.base_url + self._adapter.chat_path,
                payload=payload,
                headers=headers,
                timeout_seconds=min(
                    self._config.request_timeout_seconds,
                    request.timeout_ms / 1000.0,
                ),
                max_response_bytes=self._config.max_response_bytes,
                cancellation=token,
            )
            if result.status_code < 200 or result.status_code >= 300:
                raise TransportError(
                    f"Statut HTTP inattendu: {result.status_code}",
                    status_code=result.status_code,
                    retryable=result.status_code in {408, 425, 429, 500, 502, 503, 504},
                )
            return self._adapter.decode_chat(request, result.payload)

        response = self._retry.run(perform, token)
        token.raise_if_cancelled()
        self._cache.put(key, response)
        return response

    @staticmethod
    def _cache_key(request: AiRequest) -> str:
        canonical = {
            "operation": request.operation,
            "model": request.model,
            "messages": [
                {"role": message.role, "content": message.content}
                for message in request.messages
            ],
            "max_output_tokens": request.max_output_tokens,
        }
        encoded = json.dumps(
            canonical, sort_keys=True, ensure_ascii=False, separators=(",", ":")
        ).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()
