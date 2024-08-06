"""
tests factorial program with 3 test cases using unit test
"""
import unittest
import factorial

class TestFactorial(unittest.TestCase):
    """
    class having 3 test cases for factorial module
    """
    def test_factorial_4(self):
        """
        test case 1
        """
        actual_output = factorial.factorial(0)
        self.assertEqual(actual_output, 1)

    def test_factorial_7(self):
        """
        test case 1
        """
        actual_output = factorial.factorial(4)
        self.assertEqual(actual_output, 24)

    def test_factorial_0(self):
        """
        test case 1
        """
        actual_output = factorial.factorial(0)
        self.assertEqual(actual_output, 1)
