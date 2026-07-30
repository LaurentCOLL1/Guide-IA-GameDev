import unittest

from asteria_ai.cache import TTLCache
from asteria_ai.contracts import AiMessage, AiRequest
from asteria_ai.errors import QueueFullError, SafetyError
from asteria_ai.queue import BoundedTaskQueue
from asteria_ai.safety import SafetyPolicy


class CacheQueueSafetyTests(unittest.TestCase):
    def test_cache_expires_and_evicts(self):
        now = [10.0]
        cache = TTLCache(max_entries=1, ttl_seconds=2.0, clock=lambda: now[0])
        cache.put("a", 1)
        self.assertEqual(cache.get("a"), 1)
        cache.put("b", 2)
        self.assertIsNone(cache.get("a"))
        now[0] = 13.0
        self.assertIsNone(cache.get("b"))

    def test_queue_backpressure_and_cancellation(self):
        queue = BoundedTaskQueue(max_size=1)
        queue.submit("a", {"value": 1})
        with self.assertRaises(QueueFullError):
            queue.submit("b", {"value": 2})
        self.assertTrue(queue.cancel("a"))
        self.assertIsNone(queue.pop())

    def test_safety_rejects_control_character(self):
        request = AiRequest.chat(
            request_id="req",
            model="mock-model",
            messages=[AiMessage("user", "bad\x00value")],
        )
        with self.assertRaises(SafetyError):
            SafetyPolicy().validate_request(request)

    def test_redaction(self):
        value = SafetyPolicy.redact_text("Authorization: Bearer abcdefghijklmnop")
        self.assertNotIn("abcdefghijklmnop", value)


if __name__ == "__main__":
    unittest.main()
