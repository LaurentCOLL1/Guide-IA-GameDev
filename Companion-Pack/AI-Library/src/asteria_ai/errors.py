class AiLibraryError(Exception):
    """Erreur de base du pack."""


class ConfigurationError(AiLibraryError):
    pass


class SafetyError(AiLibraryError):
    pass


class CancelledError(AiLibraryError):
    pass


class ProtocolError(AiLibraryError):
    pass


class QueueFullError(AiLibraryError):
    pass


class TransportError(AiLibraryError):
    def __init__(self, message: str, *, status_code: int | None = None, retryable: bool = False):
        super().__init__(message)
        self.status_code = status_code
        self.retryable = retryable
