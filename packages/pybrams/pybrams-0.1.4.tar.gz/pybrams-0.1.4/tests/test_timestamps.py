import unittest
import autograd.numpy as np
from pybrams.processing.pps import Timestamps


class TestTimestamps(unittest.TestCase):
    def setUp(self):
        # Create some sample data for testing
        self.data = np.array([1000000, 2000000, 3000000])
        self.timestamps = Timestamps(self.data)

    def test_get_s(self):
        # Test the get_s method
        result = self.timestamps.s
        expected = np.array([1.0, 2.0, 3.0])
        self.assertTrue(np.array_equal(result, expected))

    def test_get_ms(self):
        # Test the get_ms method
        result = self.timestamps.ms
        expected = np.array([1000.0, 2000.0, 3000.0])
        self.assertTrue(np.array_equal(result, expected))

    def test_get_us(self):
        # Test the get_us method
        result = self.timestamps.us
        self.assertTrue(np.array_equal(result, self.data))

    def test_set_s(self):
        # Test the set_s method
        new_data = np.array([4.0, 5.0, 6.0])
        self.timestamps.set_s(new_data)
        result = self.timestamps.data
        expected = np.array([4000000, 5000000, 6000000])
        self.assertTrue(np.array_equal(result, expected))

    def test_set_ms(self):
        # Test the set_ms method
        new_data = np.array([4000.0, 5000.0, 6000.0])
        self.timestamps.set_ms(new_data)
        result = self.timestamps.data
        expected = np.array([4000000, 5000000, 6000000])
        self.assertTrue(np.array_equal(result, expected))

    def test_set_us(self):
        # Test the set_us method
        new_data = np.array([4000000, 5000000, 6000000])
        self.timestamps.set_us(new_data)
        result = self.timestamps.data
        self.assertTrue(np.array_equal(result, new_data))


if __name__ == "__main__":
    unittest.main()
