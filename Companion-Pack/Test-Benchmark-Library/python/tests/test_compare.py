import unittest
from benchmark_library.compare import compare_results

BASE={"benchmark_id":"BMK-X","contract_version":"1","implementation":"x","metric":"elapsed","unit":"ns","seed":1,"parameters":{"n":1},"environment":{"environment_id":"a"*64},"statistics":{"median":100}}
class CompareTests(unittest.TestCase):
    def test_same_environment(self):
        result=compare_results(BASE,dict(BASE))
        self.assertEqual(result["status"],"comparable"); self.assertEqual(result["delta_pct"],0)
    def test_different_environment(self):
        other={**BASE,"environment":{"environment_id":"b"*64}}
        self.assertEqual(compare_results(BASE,other)["status"],"not-comparable")
    def test_different_contract(self):
        other={**BASE,"contract_version":"2"}
        self.assertEqual(compare_results(BASE,other)["status"],"not-comparable")
