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
    
    # Check stability
    for man, woman in result.items():
        # Find man and woman's full preference lists
        man_pref_list = next(pref for pref in men_preferences if pref[0] == man)
        woman_pref_list = next(pref for pref in women_preferences if pref[0] == woman)
        
        # Get man's ranking of current woman and other possible partners
        current_woman_rank = man_pref_list.index(woman)
        
        # Check if any preferred woman would prefer this man
        man_current_woman_rank = woman_pref_list.index(man)
        
        for potential_woman in man_pref_list[1:current_woman_rank+1]:
            # Find the index of this potential woman in preference lists
            potential_woman_pref_list = next(pref for pref in women_preferences if pref[0] == potential_woman)
            
            # Check her current partner
            current_woman_partner = next(m for m, w in result.items() if w == potential_woman)
            
            # Compare rankings
            woman_potential_man_rank = potential_woman_pref_list.index(man)
            current_woman_partner_rank = potential_woman_pref_list.index(current_woman_partner)
            
            # Assert that for a woman who might prefer this man, her current partner is more preferred
            assert current_woman_partner_rank < woman_potential_man_rank, f"Instability found between {man} and {potential_woman}"