import unittest
import autograd.numpy as np
from pybrams.processing import pps  # Import the PPS class from your module

class TestPPS(unittest.TestCase):

    def setUp(self):

        # Create some sample data for testing
        self.index = np.array([1, 2, 3, 4, 5])
        self.time = np.array([100, 200, 300, 400, 500])
        self.pps = pps.PPS(self.index, self.time)

    def test_init(self):

        # Test the __init__ method
        self.assertTrue(np.array_equal(self.pps.index, self.index))
        self.assertTrue(np.array_equal(self.pps.time, self.time))
        self.assertIsNotNone(self.pps.timestamps)
        self.assertIsNotNone(self.pps.datetime)
        self.assertIsNotNone(self.pps.dt)
        self.assertIsNotNone(self.pps.di)

if __name__ == '__main__':

    unittest.main()
