import unittest
from benchmark_library.validation import validate_result

class ValidationTests(unittest.TestCase):
    def valid(self):
        return {"benchmark_id":"BMK-X","contract_version":"1","generated_at_utc":"2026-07-30T10:00:00Z","environment":{"environment_id":"a"*64},"samples":[{"status":"pass"},{"status":"pass"}],"statistics":{"count":2,"mean":1,"median":1,"variance":0,"stdev":0,"coefficient_of_variation":0,"p95":1,"p99":1},"oracle_status":"pass","comparability":"same-environment-only"}
    def test_valid(self): self.assertEqual(validate_result(self.valid()),[])
    def test_timestamp(self):
        value=self.valid(); value["generated_at_utc"]="bad"
        self.assertIn("invalid:generated_at_utc",validate_result(value))
    def test_unsafe_environment(self):
        value=self.valid(); value["environment"]["hostname"]="x"
        self.assertTrue(any("unsafe" in e for e in validate_result(value)))
