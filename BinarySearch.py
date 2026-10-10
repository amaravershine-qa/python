def binary_search_iterative(arr, target):
    left = 0
    right = len(arr) - 1

    # Keep searching while the search boundaries are valid
    while left <= right:
        # Find the middle index
        mid = (left + right) // 2
        
        # Check if the target is present at the mid index
        if arr[mid] == target:
            return mid
        
        # If target is smaller than mid, look at the left half
        elif arr[mid] > target:
            right = mid - 1
            
        # If target is larger than mid, look at the right half
        else:
            left = mid + 1
            
    # Target was not found in the array
    return -1

my_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_val = 23

result = binary_search_iterative(my_list, target_val)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list.")