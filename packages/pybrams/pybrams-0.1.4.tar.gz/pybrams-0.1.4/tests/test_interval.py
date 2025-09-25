import unittest
import datetime
from pybrams.utils import interval


class TestInterval(unittest.TestCase):
    def test_valid_interval(self):
        # Test a valid interval string
        interval_str = "2023-01-01T12:00:00/2023-01-02T12:00:00"
        result = interval.Interval.from_string(interval_str)
        assert isinstance(result, interval.Interval)
        self.assertIsInstance(result, interval.Interval)
        expected_start = datetime.datetime(
            2023, 1, 1, 12, 0, 0, tzinfo=datetime.timezone.utc
        )
        expected_end = datetime.datetime(
            2023, 1, 2, 12, 0, 0, tzinfo=datetime.timezone.utc
        )
        self.assertEqual((result.start, result.end), (expected_start, expected_end))

    def test_valid_single_datetime(self):
        # Test a valid interval string with a single datetime
        interval_str = "2023-01-01T12:00:00"
        result = interval.Interval.from_string(interval_str)
        assert isinstance(result, datetime.datetime)
        self.assertIsInstance(result, datetime.datetime)
        expected_start = datetime.datetime(
            2023, 1, 1, 12, 0, 0, tzinfo=datetime.timezone.utc
        )
        self.assertEqual(result, expected_start)

    def test_invalid_interval(self):
        # Test an invalid interval string
        interval_str = "invalid_interval"
        self.assertRaises(
            interval.InvalidIntervalError, interval.Interval.from_string, interval_str
        )


if __name__ == "__main__":
    unittest.main()
