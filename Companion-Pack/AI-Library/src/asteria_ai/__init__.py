"""API publique du Pack 3 — AI Library."""

from .cancellation import CancellationToken
from .client import AiClient
from .config import AiClientConfig, ProviderKind
from .contracts import AiError, AiMessage, AiRequest, AiResponse
from .errors import (
    AiLibraryError,
    CancelledError,
    ConfigurationError,
    ProtocolError,
    QueueFullError,
    SafetyError,
    TransportError,
)

__all__ = [
    "AiClient",
    "AiClientConfig",
    "AiError",
    "AiLibraryError",
    "AiMessage",
    "AiRequest",
    "AiResponse",
    "CancellationToken",
    "CancelledError",
    "ConfigurationError",
    "ProtocolError",
    "ProviderKind",
    "QueueFullError",
    "SafetyError",
    "TransportError",
]
