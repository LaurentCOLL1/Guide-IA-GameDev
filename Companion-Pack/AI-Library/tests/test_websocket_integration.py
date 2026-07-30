import unittest

from asteria_ai.mock_server import MockServers
from asteria_ai.websocket import WebSocketTextClient


class WebSocketIntegrationTests(unittest.TestCase):
    def test_correlated_event(self):
        with MockServers() as servers:
            client = WebSocketTextClient(servers.websocket_url)
            try:
                client.connect()
                client.send_json({"request_id": "ws-1", "subscribe": "task.progress"})
                event = client.receive_json()
            finally:
                client.close()
            self.assertEqual(event["request_id"], "ws-1")
            self.assertEqual(event["event"], "task.progress")
            self.assertEqual(event["payload"]["provider"], "mock-provider")


if __name__ == "__main__":
    unittest.main()
