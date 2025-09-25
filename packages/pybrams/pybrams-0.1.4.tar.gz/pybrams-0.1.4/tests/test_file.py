import unittest
import pybrams.brams.location
import pybrams.brams.system
import pybrams.brams.file
from pybrams.utils.interval import Interval


class TestFiles(unittest.TestCase):
    def test_get_file_location(self):
        f = pybrams.brams.file.get(
            Interval.from_string("2023-10-01T00:00"), "BEHUMA_SYS001"
        )
        location = f["BEHUMA_SYS001"][0].location
        self.assertIsInstance(location, pybrams.brams.location.Location)

    def test_get_file_system(self):
        f = pybrams.brams.file.get(
            Interval.from_string("2023-10-01T00:00"), "BEHUMA_SYS001"
        )
        system = f["BEHUMA_SYS001"][0].system
        self.assertIsInstance(system, pybrams.brams.system.System)

    def test_get_valid_file_start(self):
        f = pybrams.brams.file.get(
            Interval.from_string("2023-10-01T00:00"), "BEHUMA_SYS001"
        )
        self.assertIsInstance(f, dict)
        self.assertTrue(
            all(
                isinstance(k, str)
                and isinstance(v, list)
                and all(isinstance(item, pybrams.brams.file.File) for item in v)
                for k, v in f.items()
            )
        )

        s = pybrams.brams.system.get("BEHUMA_SYS001")["BEHUMA_SYS001"]
        f = pybrams.brams.file.get(Interval.from_string("2023-10-01T00:00"), s)
        self.assertIsInstance(f, dict)

        s = pybrams.brams.system.get(location="BEHUMA")
        f = pybrams.brams.file.get(Interval.from_string("2023-10-01T00:00"), s.keys())

        self.assertIsInstance(f, dict)

        for key, value in f.items():
            self.assertIsInstance(key, str)
            self.assertIsInstance(value, list)

        f = pybrams.brams.file.get(Interval.from_string("2023-10-01T00:00"), s.values())
        self.assertIsInstance(f, dict)

        for key, value in f.items():
            self.assertIsInstance(key, str)
            self.assertIsInstance(value, list)

    def test_get_valid_file_interval(self):
        f = pybrams.brams.file.get(
            Interval.from_string("2023-10-01T00:00/2023-10-01T00:20"), "BEHUMA_SYS001"
        )
        self.assertIsInstance(f, dict)

        s = pybrams.brams.system.get("BEHUMA_SYS001")["BEHUMA_SYS001"]
        f = pybrams.brams.file.get(
            Interval.from_string("2023-10-01T00:00/2023-10-01T00:20"), s
        )
        self.assertIsInstance(f, dict)

        s = pybrams.brams.system.get(location="BEHUMA")
        f = pybrams.brams.file.get(
            Interval.from_string("2023-10-01T00:00/2023-10-01T00:20"), s.keys()
        )
        self.assertIsInstance(f, dict)

        for key, value in f.items():
            self.assertIsInstance(key, str)
            self.assertIsInstance(value, list)

            for element in value:
                self.assertIsInstance(element, pybrams.brams.file.File)

        f = pybrams.brams.file.get(
            Interval.from_string("2023-10-01T00:00/2023-10-01T00:20"), s.values()
        )
        self.assertIsInstance(f, dict)

        for key, value in f.items():
            self.assertIsInstance(key, str)
            self.assertIsInstance(value, list)

            for element in value:
                self.assertIsInstance(element, pybrams.brams.file.File)

    def test_get_invalid_file(self):
        self.assertRaises(
            ValueError,
            pybrams.brams.file.get,
            Interval.from_string("2023-10-01T00:00/2023-10-01T00:20"),
            "INVALID",
        )


if __name__ == "__main__":
    unittest.main()
