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
    
    # Check stability by verifying no blocking pair exists
    for man, woman in result.items():
        # Find man and woman's preference lists
        man_pref_list = next(pref for pref in men_preferences if pref[0] == man)
        woman_pref_list = next(pref for pref in women_preferences if pref[0] == woman)
        
        # Find the current match's ranking for both man and woman
        current_woman_rank = man_pref_list.index(woman)
        current_man_rank = woman_pref_list.index(man)
        
        # Check all preferred matches
        for potential_man in man_pref_list[1:current_woman_rank+1]:
            for potential_woman in women_preferences:
                # Skip if this is not a valid potential match
                if potential_woman[0] not in man_pref_list:
                    continue
                
                # Find these people's current matches
                current_potential_woman_match = next(m for m, w in result.items() if w == potential_woman[0])
                
                # Get their rankings
                potential_man_rank = potential_woman.index(potential_man)
                current_match_rank = potential_woman.index(current_potential_woman_match)
                
                # Check for potential blocking pair
                assert not (potential_man_rank < current_match_rank and 
                            man_pref_list.index(potential_woman[0]) < current_woman_rank), \
                    f"Blocking pair found: {man} prefers {potential_woman[0]} and {potential_woman[0]} prefers {potential_man}"