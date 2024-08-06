"""
This module provides a function to calculate the factorial of a number.
"""

def factorial(num: int) -> int:
    """
    Function to calculate the factorial of a number.

    Args:
        num (int): The number for which to calculate the factorial.

    Returns:
        int: The factorial of the given number.
    """
    if num <= 1:
        return 1
    return num * factorial(num - 1)
