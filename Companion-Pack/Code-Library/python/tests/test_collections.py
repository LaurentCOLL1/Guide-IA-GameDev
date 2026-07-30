import unittest
from asteria_code import StableUniqueList

class StableUniqueListTests(unittest.TestCase):
    def test_preserves_order_and_rejects_duplicate(self):
        values = StableUniqueList()
        self.assertTrue(values.add("a", 1))
        self.assertTrue(values.add("b", 2))
        self.assertFalse(values.add("a", 9))
        self.assertEqual(values.values(), [1, 2])

    def test_replace_and_remove(self):
        values = StableUniqueList()
        values.add("a", 1)
        self.assertTrue(values.replace("a", 3))
        self.assertEqual(values.get("a"), 3)
        self.assertTrue(values.remove("a"))
        self.assertFalse(values.contains("a"))
