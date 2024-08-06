"""
tests factorial program with 3 test casesn using pytest
"""
import list_square

def test_square_of_list():
    """
    test case 1
    """
    result = list_square.square_of_list([1, 2, 3, 4])
    assert result == [1, 4, 9, 16]

def test_square_of_list1():
    """
    test case 2
    """
    result = list_square.square_of_list([0, 4, 1, 6])
    assert result == [0, 16, 1, 36]
