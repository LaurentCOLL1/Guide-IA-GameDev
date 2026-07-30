from __future__ import annotations

from dataclasses import dataclass

from .config import ProviderKind
from .openai_compatible import OpenAICompatibleAdapter


@dataclass(frozen=True)
class ProviderDescriptor:
    kind: ProviderKind
    display_name: str
    default_base_url: str
    compatibility_scope: str = "openai-compatible-conservative-subset"


_DESCRIPTORS = {
    ProviderKind.OLLAMA: ProviderDescriptor(
        ProviderKind.OLLAMA, "Ollama", "http://127.0.0.1:11434"
    ),
    ProviderKind.LLAMA_CPP: ProviderDescriptor(
        ProviderKind.LLAMA_CPP, "llama.cpp server", "http://127.0.0.1:8080"
    ),
    ProviderKind.LOCALAI: ProviderDescriptor(
        ProviderKind.LOCALAI, "LocalAI", "http://127.0.0.1:8080"
    ),
}


def descriptor(kind: ProviderKind) -> ProviderDescriptor:
    return _DESCRIPTORS[kind]


def adapter(kind: ProviderKind) -> OpenAICompatibleAdapter:
    return OpenAICompatibleAdapter(provider_id=kind.value)
