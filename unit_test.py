import unittest

from Numbers.credit_card_validator import is_credit_card_valid


class MyTestCase(unittest.TestCase):
    def test_credit_card(self):
        message = "Not valid credit number"
        self.assertEqual(is_credit_card_valid("2******444***961"), True, message)


if __name__ == '__main__':
    unittest.main()
