import unittest
import factorial
# import math

class TestQ1(unittest.TestCase):

    def test_factorial_4(self):
        actual_output = factorial.factorial(0)
        # expected_output = math.factorial(1)
        self.assertEqual(actual_output, 1)

    def test_factorial_7(self):
        actual_output = factorial.factorial(4)
        # expected_output = math.factorial(7)
        self.assertEqual(actual_output, 24)

    def test_factorial_0(self):
        actual_output = factorial.factorial(0)
        # expected_output = math.factorial(0)
        self.assertEqual(actual_output, 1)

