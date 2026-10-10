def longest_common_prefix(strs):
    # If the list is empty, return an empty string
    if not strs:
        return ""
        
    # Sort the list of strings alphabetically
    strs.sort()
    
    # Compare the first and last string after sorting
    first = strs[0]
    last = strs[-1]
    
    prefix = []
    # Loop through the characters of the shorter string
    for i in range(min(len(first), len(last))):
        # If characters match, add to prefix
        if first[i] == last[i]:
            prefix.append(first[i])
        else:
            # Break at the first mismatch
            break
            
    return "".join(prefix)

# Example usage:
words1 = ["flower", "flow", "flight","flew"]
words2 = ["dog", "donate", "donor", "door"]
words3 = ["dance","cadence","reward"]

print(f"Prefix for {words1}: '{longest_common_prefix(words1)}'")
print(f"Prefix for {words2}: '{longest_common_prefix(words2)}'")
print(f"Prefix for {words3}: '{longest_common_prefix(words3)}'")
