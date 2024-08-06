import pytest
import Q2

class TestQ2:
    def test_square_of_list(self):
        result = Q2.square_of_list([1, 2, 3, 4])
        assert result == [1, 4, 9, 16]

    def test_square_of_list1(self):
        result = Q2.square_of_list([0, 4, 1, 6])
        assert result == [0, 16, 1, 36]    
