from __future__ import annotations

from typing import Any

from .contracts import AiRequest, AiResponse
from .errors import ProtocolError


class OpenAICompatibleAdapter:
    def __init__(self, provider_id: str):
        self.provider_id = provider_id

    @property
    def chat_path(self) -> str:
        return "/v1/chat/completions"

    @property
    def models_path(self) -> str:
        return "/v1/models"

    def encode_chat(self, request: AiRequest) -> dict[str, Any]:
        request.validate()
        return {
            "model": request.model,
            "messages": [
                {"role": message.role, "content": message.content}
                for message in request.messages
            ],
            "max_tokens": request.max_output_tokens,
            "stream": False,
            "metadata": {
                "request_id": request.request_id,
                "client": "asteria-ai-library",
            },
        }

    def decode_chat(self, request: AiRequest, payload: dict[str, Any]) -> AiResponse:
        try:
            choice = payload["choices"][0]
            message = choice["message"]
            text = message["content"]
            model = str(payload.get("model", request.model))
            finish_reason = str(choice.get("finish_reason", "unknown"))
        except (KeyError, IndexError, TypeError) as exc:
            raise ProtocolError("Réponse OpenAI-compatible invalide.") from exc
        usage_raw = payload.get("usage", {})
        usage = {
            key: int(value)
            for key, value in usage_raw.items()
            if isinstance(value, int) and key in {"prompt_tokens", "completion_tokens", "total_tokens"}
        }
        response = AiResponse(
            request_id=request.request_id,
            provider=self.provider_id,
            model=model,
            text=str(text),
            finish_reason=finish_reason,
            usage=usage,
            raw_metadata={"object": payload.get("object"), "id": payload.get("id")},
        )
        response.validate()
        return response
