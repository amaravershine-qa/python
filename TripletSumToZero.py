def three_sum(nums):
    # Sort the array to easily manage duplicates and use two pointers
    nums.sort()
    triplets = []
    
    for i in range(len(nums) - 2):
        # Optimization: If the current number is greater than 0, 
        # the remaining numbers will also be greater than 0, so no triplet can sum to 0.
        if nums[i] > 0:
            break
            
        # Skip duplicate values for the first element to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        # Initialize two pointers for the remaining part of the array
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                triplets.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicate values for the second element
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicate values for the third element
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                # Move both pointers inward after finding a valid triplet
                left += 1
                right -= 1
                
            elif current_sum < 0:
                # Sum is too small, move the left pointer to get a larger number
                left += 1
            else:
                # Sum is too large, move the right pointer to get a smaller number
                right -= 1
                
    return triplets

# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
result = three_sum(nums)
print(f"Unique triplets that sum to zero: {result}")
