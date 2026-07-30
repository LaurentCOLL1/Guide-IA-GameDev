import unittest
from dataclasses import dataclass
from asteria_code import canonical_json_dumps, to_primitive

@dataclass
class Demo:
    z: int
    a: str

class SerializationTests(unittest.TestCase):
    def test_canonical_json(self):
        self.assertEqual(canonical_json_dumps({"z": 1, "a": 2}), '{"a":2,"z":1}')

    def test_dataclass_and_set(self):
        self.assertEqual(to_primitive(Demo(2, "x")), {"z": 2, "a": "x"})
        self.assertEqual(to_primitive({3, 1}), [1, 3])

    def test_rejects_non_finite(self):
        with self.assertRaises(ValueError):
            canonical_json_dumps(float("nan"))
