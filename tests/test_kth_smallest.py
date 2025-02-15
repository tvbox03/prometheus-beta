import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from kth_smallest import find_kth_smallest

def test_basic_functionality():
    """Test finding kth smallest element in a simple list"""
    arr = [7, 10, 4, 3, 20, 15]
    assert find_kth_smallest(arr, 3) == 7

def test_sorted_list():
    """Test with a sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert find_kth_smallest(arr, 1) == 1
    assert find_kth_smallest(arr, 5) == 5

def test_reverse_sorted_list():
    """Test with a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert find_kth_smallest(arr, 1) == 1
    assert find_kth_smallest(arr, 5) == 5

def test_list_with_duplicates():
    """Test with a list containing duplicate elements"""
    arr = [3, 3, 1, 4, 1, 5, 2]
    assert find_kth_smallest(arr, 3) == 2
    assert find_kth_smallest(arr, 4) == 3

def test_single_element_list():
    """Test with a single element list"""
    arr = [42]
    assert find_kth_smallest(arr, 1) == 42

def test_invalid_k_less_than_one():
    """Test that ValueError is raised when k is less than 1"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="k must be between 1 and 3"):
        find_kth_smallest(arr, 0)

def test_invalid_k_greater_than_list_length():
    """Test that ValueError is raised when k is greater than list length"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="k must be between 1 and 3"):
        find_kth_smallest(arr, 4)

def test_invalid_input_types():
    """Test that TypeError is raised for invalid input types"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_kth_smallest("not a list", 1)
    
    with pytest.raises(TypeError, match="k must be an integer"):
        find_kth_smallest([1, 2, 3], "not an int")