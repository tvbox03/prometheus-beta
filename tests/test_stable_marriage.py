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
        # Get man's preference list
        man_pref = men_preferences[men_preferences.index([man] + men_preferences[men_preferences.index([man] + men_preferences[0][1:])][0][1:])]
        
        # Get woman's preference list
        woman_pref = women_preferences[women_preferences.index([woman] + women_preferences[women_preferences.index([woman] + women_preferences[0][1:])][0][1:])]
        
        # Check if the current partner is the best possible
        man_current_rank = man_pref.index(woman)
        woman_current_rank = woman_pref.index(man)
        
        # Check no better matches exist
        for potential_woman in man_pref[1:man_current_rank+1]:
            potential_woman_current_partner = result.get(potential_woman)
            
            # Check woman's preference between current partner and man
            if potential_woman_current_partner:
                woman_potential_rank = woman_pref.index(potential_woman_current_partner)
                woman_man_rank = woman_pref.index(man)
                
                assert woman_potential_rank < woman_man_rank, f"Instability found between {man} and {potential_woman}"