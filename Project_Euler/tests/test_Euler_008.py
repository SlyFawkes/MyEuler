import unittest
from Project_Euler.Solutions.Project_Euler_008_Largest_product_in_a_series import *


class TestEuler008(unittest.TestCase):

    def test_find_nth_prime(self):
        self.assertEqual(biggest_adj_product(theString, 13), 23514624000)


if __name__ == '__main__':
    unittest.main()
