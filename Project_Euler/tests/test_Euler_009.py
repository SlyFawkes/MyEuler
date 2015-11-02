import unittest
from Project_Euler.Solutions.Project_Euler_009_Special_Pythagorean_triplet import *


class TestEuler009(unittest.TestCase):

    def test_special_pythagorean_triplet(self):
        self.assertEqual(special_pythagorean_triplet(), 31875000)


if __name__ == '__main__':
    unittest.main()
