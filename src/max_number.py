def find_max_number(numbers):
    """
    Find the maximum number in a given array of numbers.
    
    Args:
        numbers (list): A list of numbers to find the maximum from.
    
    Returns:
        The maximum number in the array.
    
    Raises:
        ValueError: If the input list is empty.
        TypeError: If the list contains non-numeric elements.
    """
    if not numbers:
        raise ValueError("Cannot find maximum of an empty list")
    
    try:
        return max(numbers)
    except TypeError:
        raise TypeError("List must contain only numeric elements")