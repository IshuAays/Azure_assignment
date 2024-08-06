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
    if num < 0:
        raise ValueError("Sorry, no numbers below zero")
    if num <= 1:
        output = 1
    else:
        output = num * factorial(num - 1)

    return output


if __name__ == "__main__":
    result = factorial(-3)
    print(result)
