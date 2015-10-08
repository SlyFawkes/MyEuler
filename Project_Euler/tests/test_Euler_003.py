import unittest
from Project_Euler.Solutions import Project_Euler_003_Largest_prime_factor


class TestEuler003(unittest.TestCase):

    def test_largest_prime_factor(self):
        answer = Project_Euler_003_Largest_prime_factor.largest_prime_factor(600851475143)
        self.assertEqual(answer, 6857)
