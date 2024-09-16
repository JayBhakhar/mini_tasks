import unittest
from Numbers.prime_factorization import prime_factorization


class MyTestCase(unittest.TestCase):
    def test_prime_factorization(self):
        self.assertEqual(prime_factorization(30), [2, 3, 5])
        self.assertEqual(prime_factorization(48), [2, 2, 2, 2, 3])
