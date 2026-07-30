import unittest

from asteria_ai import AiClientConfig, AiMessage, AiRequest, ProviderKind
from asteria_ai.errors import ConfigurationError, ProtocolError


class ContractsAndConfigTests(unittest.TestCase):
    def test_chat_request_validates(self):
        request = AiRequest.chat(
            request_id="req-1",
            model="mock-model",
            messages=[AiMessage("user", "Bonjour")],
        )
        request.validate()

    def test_invalid_role_is_rejected(self):
        request = AiRequest.chat(
            request_id="req-1",
            model="mock-model",
            messages=[AiMessage("tool", "non")],
        )
        with self.assertRaises(ProtocolError):
            request.validate()

    def test_remote_host_is_rejected(self):
        with self.assertRaises(ConfigurationError):
            AiClientConfig.for_provider(
                ProviderKind.OLLAMA,
                base_url="http://example.org:11434",
            )

    def test_loopback_provider_defaults_are_valid(self):
        for provider in ProviderKind:
            config = AiClientConfig.for_provider(provider)
            config.validate()


if __name__ == "__main__":
    unittest.main()
