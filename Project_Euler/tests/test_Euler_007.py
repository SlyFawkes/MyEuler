import unittest
from Project_Euler.Solutions.Project_Euler_007_10001st_prime import *


class TestEuler007(unittest.TestCase):

    def test_find_nth_prime(self):
        self.assertEqual(find_nth_prime(10001), 104743)
        self.assertEqual(find_nth_prime(0), 0)
        self.assertEqual(find_nth_prime(1), 2)
        self.assertEqual(find_nth_prime(-1), 0)


if __name__ == '__main__':
    unittest.main()
