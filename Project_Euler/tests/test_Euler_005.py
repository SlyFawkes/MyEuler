import unittest
from Project_Euler.Solutions.Project_Euler_005_Smallest_multiple import *


class TestEuler005(unittest.TestCase):

    def test_smallest_multiple(self):
        answer = smallest_multiple(20)
        self.assertEqual(answer, 232792560)


if __name__ == '__main__':
    unittest.main()
