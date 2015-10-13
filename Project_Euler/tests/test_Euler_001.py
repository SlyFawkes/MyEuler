import unittest
from Project_Euler.Solutions.Project_Euler_001_Multiples_of_3_and_5 import *


class TestEuler001(unittest.TestCase):

    def test_total_multiples(self):
        answer = total_multiples(1000)
        self.assertEqual(answer, 233168)

if __name__ == '__main__':
    unittest.main()
