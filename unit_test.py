import unittest

from Numbers.credit_card_validator import is_credit_card_valid
from Numbers.unit_converter import unit_converter


class MyTestCase(unittest.TestCase):
    def test_credit_card(self):
        message = "Not valid credit number"
        self.assertEqual(is_credit_card_valid("2******444***961"), True, message)

    def test_unit_converter(self):
        self.assertEqual(unit_converter(11, 12), "12 °C is equal to 53.6 °F")


if __name__ == '__main__':
    unittest.main()
