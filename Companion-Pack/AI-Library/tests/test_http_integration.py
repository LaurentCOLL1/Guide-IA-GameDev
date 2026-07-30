import unittest

from asteria_ai import (
    AiClient,
    AiClientConfig,
    AiMessage,
    AiRequest,
    CancellationToken,
    CancelledError,
    ProviderKind,
)
from asteria_ai.mock_server import MockServers


class HttpIntegrationTests(unittest.TestCase):
    def test_retry_then_cache(self):
        with MockServers(failures=2) as servers:
            config = AiClientConfig.for_provider(
                ProviderKind.OLLAMA,
                base_url=servers.http_url,
                max_retries=2,
                cache_ttl_seconds=60.0,
            )
            client = AiClient(config)
            request = AiRequest.chat(
                request_id="http-1",
                model="mock-model",
                messages=[AiMessage("user", "Bonjour")],
            )
            response = client.chat(request)
            self.assertEqual(response.text, "mock:Bonjour")
            self.assertEqual(response.provider, "ollama")
            self.assertEqual(servers.state.chat_calls, 3)
            cached = client.chat(request)
            self.assertEqual(cached.text, response.text)
            self.assertEqual(servers.state.chat_calls, 3)

    def test_cancellation_before_transport(self):
        with MockServers() as servers:
            config = AiClientConfig.for_provider(
                ProviderKind.LOCALAI, base_url=servers.http_url
            )
            token = CancellationToken()
            token.cancel()
            request = AiRequest.chat(
                request_id="cancel-1",
                model="mock-model",
                messages=[AiMessage("user", "Annuler")],
            )
            with self.assertRaises(CancelledError):
                AiClient(config).chat(request, token)


if __name__ == "__main__":
    unittest.main()
