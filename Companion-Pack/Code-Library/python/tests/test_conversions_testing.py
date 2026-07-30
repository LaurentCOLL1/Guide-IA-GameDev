import unittest
from asteria_code import EventRecorder, ManualClock, clamp_float, milliseconds_to_seconds, parse_bool, seconds_to_milliseconds

class ConversionTestingTests(unittest.TestCase):
    def test_conversions(self):
        self.assertEqual(clamp_float(5, 0, 3), 3)
        self.assertEqual(seconds_to_milliseconds(1.25), 1250)
        self.assertEqual(milliseconds_to_seconds(250), 0.25)
        self.assertTrue(parse_bool("yes"))
        self.assertFalse(parse_bool(0))

    def test_rejects_invalid_values(self):
        with self.assertRaises(ValueError):
            parse_bool("maybe")
        with self.assertRaises(ValueError):
            seconds_to_milliseconds(-1)

    def test_manual_clock_and_recorder(self):
        clock = ManualClock(1.0)
        self.assertEqual(clock.advance(0.5), 1.5)
        recorder = EventRecorder()
        recorder.record("hit", {"damage": 2})
        recorder.record("hit", {"damage": 3})
        self.assertEqual(recorder.count("hit"), 2)
        self.assertEqual(recorder.last("hit")[1]["damage"], 3)
