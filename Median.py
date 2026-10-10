import random

def quickselect(arr, k):
    """
    Finds the k-th smallest element in a list (0-indexed).
    """
    if len(arr) == 1:
        return arr[0]
        
    # Pick a random pivot to avoid worst-case O(n^2) performance
    pivot = random.choice(arr)
    
    # Partition the array into three parts
    lefts = [x for x in arr if x < pivot]
    middles = [x for x in arr if x == pivot]
    rights = [x for x in arr if x > pivot]
    
    # Determine which partition holds the k-th element
    if k < len(lefts):
        return quickselect(lefts, k)
    elif k < len(lefts) + len(middles):
        return middles[0]  # The k-th element falls within the middles
    else:
        # Adjust k relative to the rights subarray
        return quickselect(rights, k - len(lefts) - len(middles))


def find_median(nums):
    """
    Returns the median of a list in linear time.
    Handles both odd and even-length lists.
    """
    if not nums:
        raise ValueError("List cannot be empty")
        
    n = len(nums)
    
    # Case 1: Odd number of elements
    if n % 2 == 1:
        return quickselect(nums, n // 2)
        
    # Case 2: Even number of elements (average of two middle elements)
    else:
        mid1 = quickselect(nums, (n // 2) - 1)
        mid2 = quickselect(nums, n // 2)
        return (mid1 + mid2) / 2


# --- Driver Code to Test the Implementation ---
if __name__ == "__main__":
    test_odd = [7, 10, 4, 3, 20, 15, 8]  # Sorted: [3, 4, 7, 8, 10, 15, 20]
    test_even = [12, 3, 5, 7, 19, 1]     # Sorted: [1, 3, 5, 7, 12, 19]

    print(f"Median of {test_odd} (Odd length):")
    print(find_median(test_odd))  # Expected: 8

    print(f"\nMedian of {test_even} (Even length):")
    print(find_median(test_even))  # Expected: (5 + 7) / 2 = 6.0
