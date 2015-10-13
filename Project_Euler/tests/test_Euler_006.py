import unittest
from Project_Euler.Solutions.Project_Euler_006_Sum_square_difference import *


class TestEuler006(unittest.TestCase):

    def test_sum_square_difference(self):
        answer = sum_square_difference(100)
        self.assertEqual(answer, 25164150)

    def test_sum_of_squares(self):
        answer = sum_of_squares(100)
        self.assertEqual(answer, 338350)

    def test_square_of_sum(self):
        answer = square_of_sum(100)
        self.assertEqual(answer, 25502500)


if __name__ == '__main__':
    unittest.main()
