import pytest
from src.aho_corasick import AhoCorasick

def test_basic_pattern_matching():
    """
    Test basic pattern matching with single and multiple patterns
    """
    # Single pattern
    ac = AhoCorasick(["hello"])
    result = ac.search("hello world")
    assert result == [("hello", 0)]

    # Multiple patterns
    ac = AhoCorasick(["he", "she", "his", "hers"])
    result = ac.search("he and she and his and hers")
    expected = [
        ("he", 0), 
        ("he", 8), 
        ("she", 7), 
        ("his", 15), 
        ("hers", 24)
    ]
    assert sorted(result) == sorted(expected)

def test_overlapping_patterns():
    """
    Test overlapping pattern matching
    """
    ac = AhoCorasick(["ab", "bc", "bca"])
    result = ac.search("abcba")
    expected = [
        ("ab", 0), 
        ("bc", 1), 
        ("bca", 1)
    ]
    assert sorted(result) == sorted(expected)

def test_no_matches():
    """
    Test case with no pattern matches
    """
    ac = AhoCorasick(["hello", "world"])
    result = ac.search("python")
    assert result == []

def test_case_sensitivity():
    """
    Verify case-sensitive matching
    """
    ac = AhoCorasick(["Hello", "hello"])
    result = ac.search("hello Hello")
    expected = [
        ("hello", 0), 
        ("Hello", 6)
    ]
    assert sorted(result) == sorted(expected)

def test_empty_input():
    """
    Test matching with empty text
    """
    ac = AhoCorasick(["test"])
    result = ac.search("")
    assert result == []

def test_large_input():
    """
    Test performance with a larger input
    """
    patterns = ["cat", "dog", "mouse"]
    text = "the cat sat on the dog while the mouse played"
    ac = AhoCorasick(patterns)
    result = ac.search(text)
    expected = [
        ("cat", 4), 
        ("dog", 20), 
        ("mouse", 35)
    ]
    assert sorted(result) == sorted(expected)