import unittest
from Project_Euler.Solutions.Project_Euler_003_Largest_prime_factor import *


class TestEuler003(unittest.TestCase):

    def test_largest_prime_factor(self):
        answer = largest_prime_factor(600851475143)
        self.assertEqual(answer, 6857)

if __name__ == '__main__':
    unittest.main()
