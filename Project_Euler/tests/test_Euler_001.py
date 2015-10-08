import unittest
from Project_Euler.Solutions import Project_Euler_001_Multiples_of_3_and_5


class TestEuler001(unittest.TestCase):

    def test_total_multiples(self):
        answer = Project_Euler_001_Multiples_of_3_and_5.total_multiples(1000)
        self.assertEqual(answer, 233168)
