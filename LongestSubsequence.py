import bisect  # 1. Import Python's built-in "searching tool"

def longest_increasing_subsequence(nums):
    if not nums:
        return 0  # If the list is empty, the length is 0!
        
    tails = []    # 2. This list represents the top cards of our piles
    
    for num in nums:  # 3. Look at each number in our input list, one by one
        
        # 4. Use a super-fast "Binary Search" to scan our piles (tails)
        # It finds the index (idx) of the first pile whose top card is >= num
        idx = bisect.bisect_left(tails, num)
        
        # 5. If idx matches the length of tails, it means our number is bigger
        # than the top card of EVERY pile. We create a NEW pile!
        if idx == len(tails):
            tails.append(num)
            
        # 6. Otherwise, we place our number on top of an existing pile,
        # updating its value to be smaller and more optimized.
        else:
            tails[idx] = num
            
    # 7. The total number of piles we created is our final answer!
    return len(tails)
result = longest_increasing_subsequence([10, 9, 2, 5, 3, 7])
print(result)