def find_kth_smallest(arr, k):
    """
    Find the kth smallest element in an array using quickselect algorithm.
    
    Args:
        arr (list): Input list of numbers
        k (int): The k-th smallest element to find (1-based index)
    
    Returns:
        The kth smallest element in the array
    
    Raises:
        ValueError: If k is less than 1 or greater than the array length
        TypeError: If input types are incorrect
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    
    # Check k is within valid range
    if k < 1 or k > len(arr):
        raise ValueError(f"k must be between 1 and {len(arr)}")
    
    def partition(left, right, pivot_index):
        """Partition the array and return the pivot's final position"""
        pivot = arr[pivot_index]
        # Move pivot to end
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        
        # Partition around pivot
        store_index = left
        for i in range(left, right):
            if arr[i] < pivot:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        
        # Move pivot to its final place
        arr[right], arr[store_index] = arr[store_index], arr[right]
        
        return store_index
    
    def quickselect(left, right):
        """Find kth smallest using quickselect"""
        # If the list contains only one element, return that element
        if left == right:
            return arr[left]
        
        # Select a random pivot_index between left and right
        import random
        pivot_index = random.randint(left, right)
        
        # Partition around the pivot
        pivot_index = partition(left, right, pivot_index)
        
        # The pivot is in its final sorted position
        if k - 1 == pivot_index:
            return arr[pivot_index]
        # If k is less than pivot position, search left side
        elif k - 1 < pivot_index:
            return quickselect(left, pivot_index - 1)
        # If k is greater than pivot position, search right side
        else:
            return quickselect(pivot_index + 1, right)
    
    return quickselect(0, len(arr) - 1)