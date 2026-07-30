import unittest
from benchmark_library.environment import safe_environment

class EnvironmentTests(unittest.TestCase):
    def test_safe_environment_has_hash(self):
        env=safe_environment({"renderer":"none"})
        self.assertEqual(len(env["environment_id"]),64)
    def test_unsafe_field_rejected(self):
        with self.assertRaises(ValueError): safe_environment({"hostname":"private"})
