import unittest
from Project_Euler.Solutions.Project_Euler_006_Sum_square_difference import *


class TestEuler006(unittest.TestCase):

    def test_sum_square_difference(self):
        self.assertEqual(sum_square_difference(100), 25164150)
        self.assertEqual(sum_square_difference(0), 0)
        self.assertEqual(sum_square_difference(-1), 0)

    def test_sum_of_squares(self):
        self.assertEqual(sum_of_squares(100), 338350)
        self.assertEqual(sum_of_squares(0), 0)
        self.assertEqual(sum_of_squares(-1), 0)

    def test_square_of_sum(self):
        self.assertEqual(square_of_sum(100), 25502500)
        self.assertEqual(square_of_sum(0), 0)
        self.assertEqual(square_of_sum(-1), 0)


if __name__ == '__main__':
    unittest.main()
