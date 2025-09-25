import unittest
import pybrams.brams.location


class TestLocations(unittest.TestCase):
    def test_get_valid_location(self):
        location = pybrams.brams.location.get("BEHUMA")
        self.assertIsInstance(location, pybrams.brams.location.Location)
        self.assertEqual(location.location_code, "BEHUMA")
        self.assertIsInstance(location.location_code, str)
        self.assertIsInstance(location.name, str)
        self.assertIsInstance(location.status, str)
        self.assertIsInstance(location.longitude, float)
        self.assertIsInstance(location.latitude, float)
        self.assertIsInstance(location.altitude, float)
        self.assertIsInstance(location.systems_url, str)

    def test_get_invalid_location(self):
        self.assertRaises(ValueError, pybrams.brams.location.get, "INVALID")

    def test_all_returns_dict(self):
        locations_dict = pybrams.brams.location.all()
        self.assertIsInstance(locations_dict, dict)

    def test_all_contains_locations(self):
        locations_dict = pybrams.brams.location.all()
        self.assertIn("BEHUMA", locations_dict)
        self.assertIn("BENEUF", locations_dict)
        self.assertIn("BEOPHA", locations_dict)
        self.assertIn("BEOVER", locations_dict)
        self.assertIn("BETRUI", locations_dict)


if __name__ == "__main__":
    unittest.main()
