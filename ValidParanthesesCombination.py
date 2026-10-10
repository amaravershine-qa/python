def generate_parentheses(n):
    """
    Generates all combinations of well-formed parentheses for n pairs.
    """
    result = []
    
    def backtrack(current_str, open_count, close_count):
        # Base Case: If the current string reaches the maximum length, it's valid
        if len(current_str) == 2 * n:
            result.append(current_str)
            return
        
        # Rule 1: We can always add an open parenthesis if we haven't used all of them
        if open_count < n:
            backtrack(current_str + '(', open_count + 1, close_count)
            
        # Rule 2: We can only add a close parenthesis if it won't violate the balance
        if close_count < open_count:
            backtrack(current_str + ')', open_count, close_count + 1)
            
    # Start the recursion with an empty string and 0 counts
    backtrack("", 0, 0)
    return result

# --- Driver Code to Test the Implementation ---
if __name__ == "__main__":
    pairs = 3
    combinations = generate_parentheses(pairs)
    
    print(f"Total valid combinations for {pairs} pairs: {len(combinations)}")
    print("Combinations:")
    for comb in combinations:
        print(comb)



