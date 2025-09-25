import unittest
import pybrams.brams.system
import pybrams.brams.location


class TestSystems(unittest.TestCase):
    def test_get_system_by_location(self):
        location = pybrams.brams.location.get("BEBILZ")
        system = pybrams.brams.system.get(location=location)["BEBILZ_SYS001"]
        self.assertIsInstance(system, pybrams.brams.system.System)
        self.assertIsInstance(system.system_code, str)
        self.assertIsInstance(system.name, str)
        self.assertIsInstance(system.start, str)
        self.assertIsInstance(system.end, str)
        self.assertIsInstance(system.antenna, int)
        self.assertIsInstance(system.location_url, str)
        self.assertIsInstance(system.location_code, str)
        location = pybrams.brams.location.get("BEHUMA")
        system = pybrams.brams.system.get(location=location)

        self.assertIsInstance(system, dict)

    def test_get_system_by_system_code(self):
        system = pybrams.brams.system.get(system_code="BEHUMA_SYS001")["BEHUMA_SYS001"]
        self.assertIsInstance(system, pybrams.brams.system.System)
        self.assertIsInstance(system.system_code, str)
        self.assertIsInstance(system.name, str)
        self.assertIsInstance(system.start, str)
        self.assertIsInstance(system.end, str)
        self.assertIsInstance(system.antenna, int)
        self.assertIsInstance(system.location_url, str)
        self.assertIsInstance(system.location_code, str)

    def test_get_invalid_system(self):
        self.assertRaises(ValueError, pybrams.brams.system.get, system_code="INVALID")
        self.assertRaises(ValueError, pybrams.brams.system.get, location=None)

    def test_all_contains_systems(self):
        systems_dict = pybrams.brams.system.all()
        expected_system_codes = [
            "BEHUMA_SYS001",
            "BEHUMA_SYS002",
            "BEHUMA_SYS003",
            "BEHUMA_SYS004",
            "BEHUMA_SYS005",
            "BEHUMA_SYS006",
        ]

        for system_code in expected_system_codes:
            self.assertIn(system_code, systems_dict)


if __name__ == "__main__":
    unittest.main()
