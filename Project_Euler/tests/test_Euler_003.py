import unittest
from Project_Euler.Solutions.Project_Euler_003_Largest_prime_factor import *


class TestEuler003(unittest.TestCase):

    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor(600851475143), 6857)
        self.assertEqual(largest_prime_factor(0), 0)
        self.assertEqual(largest_prime_factor(1), 0)
        self.assertEqual(largest_prime_factor(-1), 0)

if __name__ == '__main__':
    unittest.main()
