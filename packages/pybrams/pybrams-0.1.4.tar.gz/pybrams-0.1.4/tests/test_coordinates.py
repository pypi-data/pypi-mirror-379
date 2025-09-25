import unittest
from pybrams.utils.coordinates import GeodeticCoordinates, CartesianCoordinates, Coordinates

class TestGeodeticCoordinates(unittest.TestCase):

    def test_add(self):

        coords1 = GeodeticCoordinates(50.0, 4.0, 0.0)
        coords2 = GeodeticCoordinates(1.0, 2.0, 3.0)
        result = coords1 + coords2
        expected = GeodeticCoordinates(51.0, 6.0, 3.0)
        self.assertEqual(result, expected)

    def test_sub(self):

        coords1 = GeodeticCoordinates(50.0, 4.0, 0.0)
        coords2 = GeodeticCoordinates(1.0, 2.0, 3.0)
        result = coords1 - coords2
        expected = GeodeticCoordinates(49.0, 2.0, -3.0)
        self.assertEqual(result, expected)

class TestCartesianCoordinates(unittest.TestCase):

    def test_add(self):

        coords1 = CartesianCoordinates(1.0, 2.0, 3.0)
        coords2 = CartesianCoordinates(4.0, 5.0, 6.0)
        result = coords1 + coords2
        expected = CartesianCoordinates(5.0, 7.0, 9.0)
        self.assertEqual(result, expected)

    def test_sub(self):

        coords1 = CartesianCoordinates(1.0, 2.0, 3.0)
        coords2 = CartesianCoordinates(4.0, 5.0, 6.0)
        result = coords1 - coords2
        expected = CartesianCoordinates(-3.0, -3.0, -3.0)
        self.assertEqual(result, expected)

class TestCoordinates(unittest.TestCase):

    def test_geodetic2Geocentric(self):

        coords = GeodeticCoordinates(50.0, 4.0, 0.0)
        result = Coordinates.geodetic2Geocentric(coords)

        # Mock expected values for testing
        expected = CartesianCoordinates(4097.85754074113, 286.550113622701, 4862.789037706432)

        self.assertEqual(result, expected)

    def test_geodetic2Dourbocentric(self):

        coords = GeodeticCoordinates(50.0, 4.0, 0.0)
        result = Coordinates.geodetic2Dourbocentric(coords)

        # Mock expected values for testing
        expected = CartesianCoordinates(-42.10692893814187, -11.018530989892481, -0.018761101551043897)

        self.assertEqual(result, expected)

    def test_fromGeodetic(self):

        latitude = 50.0
        longitude = 4.0
        altitude = 0.0
        result = Coordinates.fromGeodetic(latitude, longitude, altitude)

        # Mock expected values for testing
        expected_geodetic = GeodeticCoordinates(50.0, 4.0, 0.0)
        expected_geocentric = CartesianCoordinates(4097.85754074113, 286.550113622701, 4862.789037706432)
        expected_dourbocentric = CartesianCoordinates(-42.10692893814187, -11.018530989892481, -0.018761101551043897)
        expected = Coordinates(expected_geodetic, expected_geocentric, expected_dourbocentric)

        self.assertEqual(result, expected)


if __name__ == '__main__':

    unittest.main()
