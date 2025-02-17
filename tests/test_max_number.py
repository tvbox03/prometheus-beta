import pytest
from src.max_number import find_max_number

def test_find_max_number_positive():
    assert find_max_number([1, 2, 3, 4, 5]) == 5

def test_find_max_number_negative():
    assert find_max_number([-1, -2, -3, -4, -5]) == -1

def test_find_max_number_mixed():
    assert find_max_number([-10, 0, 10, 5, -5]) == 10

def test_find_max_number_single_element():
    assert find_max_number([42]) == 42

def test_find_max_number_duplicate_max():
    assert find_max_number([5, 5, 5, 5]) == 5

def test_find_max_number_empty_list():
    with pytest.raises(ValueError, match="Cannot find maximum of an empty list"):
        find_max_number([])

def test_find_max_number_non_numeric():
    with pytest.raises(TypeError, match="List must contain only numeric elements"):
        find_max_number([1, 2, 'three', 4])

def test_find_max_number_float():
    assert find_max_number([1.5, 2.7, 0.3, 4.2]) == 4.2