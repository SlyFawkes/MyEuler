import unittest
from Project_Euler.Solutions.Project_Euler_001_Multiples_of_3_and_5 import *


class TestEuler001(unittest.TestCase):

    def test_total_multiples(self):
        self.assertEqual(total_multiples(1000), 233168)
        self.assertEqual(total_multiples(0), 0)
        self.assertEqual(total_multiples(1), 0)
        self.assertEqual(total_multiples(-1), 0)

if __name__ == '__main__':
    unittest.main()
