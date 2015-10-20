import unittest
from Project_Euler.Solutions.Project_Euler_005_Smallest_multiple import *


class TestEuler005(unittest.TestCase):

    def test_smallest_multiple(self):
        self.assertEqual(smallest_multiple(20), 232792560)
        self.assertEqual(smallest_multiple(-1), 0)
        self.assertEqual(smallest_multiple(0), 0)
        self.assertEqual(smallest_multiple(1), 1)
        self.assertEqual(smallest_multiple(2), 2)


if __name__ == '__main__':
    unittest.main()
