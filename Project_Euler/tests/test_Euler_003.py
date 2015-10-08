import unittest
from Project_Euler import Project_Euler_003_Largest_prime_factor


class TestEuler001(unittest.TestCase):

    def test_fibbonacci(self):
        answer = Project_Euler_003_Largest_prime_factor.det_first_prime(600851475143, 2)
        self.assertEqual(answer, 6857)
