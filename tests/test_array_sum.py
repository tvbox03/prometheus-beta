import pytest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.array_sum import sum_array

def test_sum_normal_array():
    """Test summing a normal array of integers"""
    assert sum_array([1, 2, 3, 4, 5]) == 15

def test_sum_empty_array():
    """Test summing an empty array"""
    assert sum_array([]) == 0

def test_sum_negative_numbers():
    """Test summing an array with negative numbers"""
    assert sum_array([-1, -2, -3]) == -6

def test_sum_mixed_numbers():
    """Test summing an array with mixed positive and negative numbers"""
    assert sum_array([-1, 0, 1]) == 0

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_array(123)

def test_invalid_element_type():
    """Test that TypeError is raised for non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_array([1, 2, '3'])