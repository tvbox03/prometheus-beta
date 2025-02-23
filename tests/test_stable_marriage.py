"""
Tests for the Stable Marriage Algorithm implementation
"""

import pytest
from src.stable_marriage import stable_marriage


def test_basic_stable_marriage():
    """Test a simple stable marriage scenario"""
    men_preferences = [
        ['m1', 'w1', 'w2', 'w3'],
        ['m2', 'w2', 'w1', 'w3'],
        ['m3', 'w3', 'w1', 'w2']
    ]
    women_preferences = [
        ['w1', 'm1', 'm2', 'm3'],
        ['w2', 'm2', 'm1', 'm3'],
        ['w3', 'm3', 'm1', 'm2']
    ]
    
    result = stable_marriage(men_preferences, women_preferences)
    
    # Verify the result is a complete matching
    assert len(result) == 3
    assert set(result.keys()) == {'m1', 'm2', 'm3'}
    assert set(result.values()) == {'w1', 'w2', 'w3'}


def test_empty_input_raises_error():
    """Test that empty inputs raise a ValueError"""
    with pytest.raises(ValueError, match="Preference lists cannot be empty"):
        stable_marriage([], [])


def test_mismatched_lengths_raises_error():
    """Test that unequal number of men and women raises an error"""
    men_preferences = [
        ['m1', 'w1', 'w2'],
        ['m2', 'w1', 'w2']
    ]
    women_preferences = [
        ['w1', 'm1', 'm2'],
    ]
    
    with pytest.raises(ValueError, match="Number of men and women must be equal"):
        stable_marriage(men_preferences, women_preferences)


def test_mismatched_names_raises_error():
    """Test that mismatched names raise an error"""
    men_preferences = [
        ['m1', 'w1', 'w2'],
        ['m2', 'w3', 'w4']
    ]
    women_preferences = [
        ['w1', 'm1', 'm3'],
        ['w2', 'm2', 'm4']
    ]
    
    with pytest.raises(ValueError, match="Names in preference lists do not match"):
        stable_marriage(men_preferences, women_preferences)


def test_stability_property():
    """
    Verify the stability property of the matching.
    No man and woman should prefer each other over their current partners.
    """
    men_preferences = [
        ['m1', 'w1', 'w2', 'w3'],
        ['m2', 'w2', 'w1', 'w3'],
        ['m3', 'w3', 'w1', 'w2']
    ]
    women_preferences = [
        ['w1', 'm1', 'm2', 'm3'],
        ['w2', 'm2', 'm1', 'm3'],
        ['w3', 'm3', 'm1', 'm2']
    ]
    
    result = stable_marriage(men_preferences, women_preferences)
    
    # Build easy lookup structures
    man_preferences = {pref[0]: pref[1:] for pref in men_preferences}
    woman_preferences = {pref[0]: pref[1:] for pref in women_preferences}
    
    # Check stability by verifying no blocking pair exists
    for man, woman in result.items():
        # Check if man prefers another woman
        for potential_woman in man_preferences[man]:
            # Man prefers this woman to current match
            if man_preferences[man].index(potential_woman) < man_preferences[man].index(woman):
                # Check if woman prefers this man
                current_man_for_woman = result[next(m for m, w in result.items() if w == potential_woman)]
                
                # If woman prefers this man over her current match
                if woman_preferences[potential_woman].index(man) < woman_preferences[potential_woman].index(current_man_for_woman):
                    pytest.fail(f"Blocking pair found: {man} prefers {potential_woman} and {potential_woman} prefers {man}")
    
    # If we get here without failing, the matching is stable