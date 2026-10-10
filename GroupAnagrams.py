from collections import defaultdict

def group_anagrams(words):
    # Initialize a dictionary where values defaults to a list
    anagram_map = defaultdict(list)
    
    for word in words:
        # Sort the letters of the word to create a unique key
        # 'sorted("eat")' returns ['a', 'e', 't']. 
        # ''.join() turns it back into the string 'aet'
        sorted_key = "".join(sorted(word))
        
        # Append the original word to the list matching that key
        anagram_map[sorted_key].append(word)
        
    # Return all grouped lists as a list of lists
    return list(anagram_map.values())

# Example usage:
word_list = ["eat", "tea", "tan", "ate", "nat", "bat", "tab"]
result = group_anagrams(word_list)

print("Grouped Anagrams:")
print(result)
