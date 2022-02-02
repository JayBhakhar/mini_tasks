import unittest

from Classic_Algorithms.collatz_conjecture import collatz_conjecture
from Numbers.credit_card_validator import is_credit_card_valid
from Numbers.unit_converter import convert_unit


class MyTestCase(unittest.TestCase):
    # def test_credit_card(self):
    #     message = "Not valid credit number"
    #     self.assertEqual(is_credit_card_valid("2******444***961"), True, message)

    def test_unit_converter(self):
        self.assertEqual(convert_unit('celsius', 'fahrenheit', 12), '12 °C is equal to 53.6 °F')
        self.assertEqual(convert_unit('fahrenheit', 'celsius', 50), '50 °F is equal to 10.0008 °C')
        self.assertEqual(convert_unit('kg', 'pound', 71), '71 Kg is equal to 156.52802 Pound')
        self.assertEqual(convert_unit('pound', 'kg', 200), '200 Pound is equal to 90.7184 Kg')

    def test_collatz_conjecture(self):
        self.assertEqual(collatz_conjecture(31), 1)
        self.assertEqual(collatz_conjecture(696), 1)
        self.assertEqual(collatz_conjecture(3111), 1)
        self.assertEqual(collatz_conjecture(91152), 1)
        self.assertEqual(collatz_conjecture(999851), 1)


if __name__ == '__main__':
    unittest.main()
