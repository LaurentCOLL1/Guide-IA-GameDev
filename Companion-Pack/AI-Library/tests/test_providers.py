import unittest

from asteria_ai.contracts import AiMessage, AiRequest
from asteria_ai.config import ProviderKind
from asteria_ai.providers import adapter, descriptor


class ProviderTests(unittest.TestCase):
    def test_common_payload_is_provider_independent(self):
        request = AiRequest.chat(
            request_id="req-provider",
            model="mock-model",
            messages=[AiMessage("user", "Même contrat")],
        )
        payloads = [adapter(kind).encode_chat(request) for kind in ProviderKind]
        self.assertEqual(payloads[0], payloads[1])
        self.assertEqual(payloads[1], payloads[2])

    def test_descriptors_use_loopback(self):
        for kind in ProviderKind:
            self.assertIn("127.0.0.1", descriptor(kind).default_base_url)


if __name__ == "__main__":
    unittest.main()
