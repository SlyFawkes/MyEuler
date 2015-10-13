import unittest
from Project_Euler.Solutions.Project_Euler_002_Even_Fibonacci_numbers import *


class TestEuler001(unittest.TestCase):

    def test_fibbonacci(self):
        answer = fibbonacci(4000000)
        self.assertEqual(answer, 4613732)

if __name__ == '__main__':
    unittest.main()
