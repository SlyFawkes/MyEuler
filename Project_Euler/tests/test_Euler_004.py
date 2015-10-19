import unittest
from Project_Euler.Solutions.Project_Euler_004_Largest_palindrome_product import *


class TestEuler004(unittest.TestCase):

    def test_check_if_palindrome(self):
        self.assertTrue(check_if_palindrome(123321))
        self.assertTrue(check_if_palindrome(0))
        self.assertTrue(check_if_palindrome(-121))
        self.assertFalse(check_if_palindrome(123456))
        self.assertFalse(check_if_palindrome(-123456))

    def test_largest_palindrome(self):
        self.assertEqual(largest_palindrome(3), 906609)
        self.assertEqual(largest_palindrome(0), 0)
        self.assertEqual(largest_palindrome(-1), 0)
        self.assertEqual(largest_palindrome(1), 9)
        self.assertEqual(largest_palindrome(2), 9009)


if __name__ == '__main__':
    unittest.main()
