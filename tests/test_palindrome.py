import unittest
from Text.palindrome import palindrome


class MyTestCase(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(palindrome('asdfgfdsa'), True)
        self.assertEqual(palindrome('raear'), True)
        self.assertEqual(palindrome('asdfgf'), False)
