import unittest
from Numbers.unit_converter import convert_unit


class MyTestCase(unittest.TestCase):
    def test_unit_converter(self):
        self.assertEqual(convert_unit('celsius', 'fahrenheit', 12), 53.6)
        self.assertEqual(convert_unit('fahrenheit', 'celsius', 50), 10.00)
        self.assertEqual(convert_unit('kg', 'pound', 170), 374.785)
        self.assertEqual(convert_unit('pound', 'kg', 200), 90.718)
        with self.assertRaises(AttributeError):
            convert_unit('kg', 'pp', 45)
