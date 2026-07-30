import unittest
from benchmark_library.stats import percentile, summarize

class StatsTests(unittest.TestCase):
    def test_percentile_edges(self):
        self.assertEqual(percentile([1,2,3],0),1)
        self.assertEqual(percentile([1,2,3],1),3)
    def test_percentile_interpolation(self):
        self.assertAlmostEqual(percentile([0,10],0.5),5)
    def test_summary_fields(self):
        result=summarize([1,2,3,4])
        self.assertEqual(result["count"],4)
        self.assertIn("variance",result)
        self.assertIn("p95",result)
    def test_empty_rejected(self):
        with self.assertRaises(ValueError): summarize([])
