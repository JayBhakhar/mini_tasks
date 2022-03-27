import unittest
from Numbers.credit_card_validator import is_credit_card_valid


class MyTestCase(unittest.TestCase):
    def test_credit_card_validator(self):
        self.assertEqual(is_credit_card_valid('4276060057073***'), True)
        self.assertEqual(is_credit_card_valid('1112223334445556'), False)
        with self.assertRaises(ValueError):
            is_credit_card_valid('123')


if __name__ == '__main__':
    unittest.main()
