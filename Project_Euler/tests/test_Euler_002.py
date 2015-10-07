import unittest
from Project_Euler.Project_Euler import Project_Euler_002_Even_Fibonacci_numbers


class TestEuler001(unittest.TestCase):

    def test_fibbonacci(self):
        answer = Project_Euler_002_Even_Fibonacci_numbers.fibbonacci(4000000)
        self.assertEqual(answer, 4613732)
