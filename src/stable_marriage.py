"""
Gale-Shapley Algorithm for Stable Marriage Problem

This module implements the Gale-Shapley algorithm to find a stable matching
between two equal-sized sets of elements.

The algorithm ensures that no pair of elements from opposite sets would both 
prefer each other over their current matched partners.
"""

from typing import List, Dict, Tuple


def stable_marriage(men_preferences: List[List[str]], 
                    women_preferences: List[List[str]]) -> Dict[str, str]:
    """
    Implement the Gale-Shapley algorithm for stable marriage problem.

    Args:
        men_preferences (List[List[str]]): Preference lists for men, 
            where each inner list contains women's names in order of preference.
        women_preferences (List[List[str]]): Preference lists for women, 
            where each inner list contains men's names in order of preference.

    Returns:
        Dict[str, str]: A stable matching where keys are men and values are 
        their matched women.

    Raises:
        ValueError: If input lists are not valid (different lengths, mismatched names, etc.)
    """
    # Validate input
    if not men_preferences or not women_preferences:
        raise ValueError("Preference lists cannot be empty")
    
    if len(men_preferences) != len(women_preferences):
        raise ValueError("Number of men and women must be equal")
    
    # Prepare data structures
    n = len(men_preferences)
    men_names = [pref[0] for pref in men_preferences]
    women_names = [pref[0] for pref in women_preferences]
    
    # Validate that names are consistent
    men_set = set(men_names)
    women_set = set(women_names)
    
    # Validate that each preference list contains the right names
    for i, (men_pref, women_pref) in enumerate(zip(men_preferences, women_preferences)):
        # Check if the first element matches the list's expected first element
        if men_pref[0] != men_names[i] or women_pref[0] != women_names[i]:
            raise ValueError("First element of each preference list must match its index")
        
        # Check that all names are present
        men_pref_names = set(men_pref[1:])
        women_pref_names = set(women_pref[1:])
        
        if men_pref_names != women_set or women_pref_names != men_set:
            raise ValueError("Names in preference lists do not match")
    
    # Create preference dictionaries for efficient lookup
    men_prefs = {men_names[i]: men_preferences[i][1:] for i in range(n)}
    women_prefs = {women_names[i]: {man: rank for rank, man in enumerate(women_preferences[i][1:])} 
                   for i in range(n)}
    
    # Initialize matching
    matching = {man: None for man in men_names}
    women_partners = {woman: None for woman in women_names}
    
    # Proposal tracking
    men_proposal_index = {man: 0 for man in men_names}
    
    # Run Gale-Shapley algorithm
    while None in matching.values():
        # Find a free man
        free_man = next(man for man, partner in matching.items() if partner is None)
        
        # Get his next preferred woman
        if men_proposal_index[free_man] >= len(men_prefs[free_man]):
            raise ValueError(f"No stable matching possible for {free_man}")
        
        woman = men_prefs[free_man][men_proposal_index[free_man]]
        men_proposal_index[free_man] += 1
        
        # Check woman's current situation
        current_partner = women_partners[woman]
        
        if current_partner is None:
            # Woman is free, accept proposal
            matching[free_man] = woman
            women_partners[woman] = free_man
        else:
            # Compare preferences
            if (women_prefs[woman].get(free_man, float('inf')) < 
                women_prefs[woman].get(current_partner, float('inf'))):
                # Woman prefers new man
                matching[free_man] = woman
                women_partners[woman] = free_man
                matching[current_partner] = None
    
    return matching