import unittest

from Numbers.fibonacci_sequence import fibonacci_sequence


class MyTestCase(unittest.TestCase):
    def test_fibonacci_sequence(self):
        self.assertEqual(fibonacci_sequence(0), 0)
        self.assertEqual(fibonacci_sequence(1), 1)
        self.assertEqual(fibonacci_sequence(2), 1)
        self.assertEqual(fibonacci_sequence(10), 55)
        with self.assertRaises(ValueError):
            fibonacci_sequence(-10)
