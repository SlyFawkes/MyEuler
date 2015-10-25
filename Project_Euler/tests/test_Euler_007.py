import unittest
from Project_Euler.Solutions.Project_Euler_007_10001st_prime import *


class TestEuler007(unittest.TestCase):

    def test_find_nth_prime(self):
        self.assertEqual(find_nth_prime(10001), 104743)


if __name__ == '__main__':
    unittest.main()
