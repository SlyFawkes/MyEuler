import unittest
from Project_Euler.Solutions.Project_Euler_004_Largest_palindrome_product import *


class TestEuler004(unittest.TestCase):

    def test_check_if_palindrome(self):
        self.assertTrue(check_if_palindrome(123321))
        self.assertFalse(check_if_palindrome(123456))

    def test_largest_palindrome(self):
        answer = largest_palindrome(3)
        self.assertEqual(answer, 906609)


if __name__ == '__main__':
    unittest.main()
