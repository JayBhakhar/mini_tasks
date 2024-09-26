import unittest
from Numbers.distance_between_two_cities import distance_between_two_cities


class MyTestCase(unittest.TestCase):
    def test_distance_between_two_cities(self):
        self.assertEqual(distance_between_two_cities("surat", "ufa", "km"), 3779.86)
        self.assertEqual(distance_between_two_cities("moscow", "ufa", "mile"), 725.86)
        self.assertEqual(distance_between_two_cities("surat", "ufa", "mile"), 2348.69)
        with self.assertRaises(AttributeError):
            distance_between_two_cities("surat", "ufa", "mi")
            distance_between_two_cities("sura", "ufa", "mile")
