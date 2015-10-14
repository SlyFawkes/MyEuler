import unittest
from Project_Euler.Solutions.Project_Euler_002_Even_Fibonacci_numbers import *


class TestEuler002(unittest.TestCase):

    def test_fibbonacci(self):
        self.assertEqual(fibbonacci(4000000), 4613732)
        self.assertEqual(fibbonacci(0), 0)
        self.assertEqual(fibbonacci(1), 0)
        self.assertEqual(fibbonacci(-1), 0)

if __name__ == '__main__':
    unittest.main()
