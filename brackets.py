def is_balanced(s: str) -> bool:
    # Map opening brackets to their matching closing brackets
    bracket_map = {'(': ')', '[': ']', '{': '}'}
    close_brackets = set(bracket_map.values())
    
    stack = []
    
    for char in s:
        if char in bracket_map:
            # If it's an opening bracket, push its expected closing pair onto the stack
            stack.append(bracket_map[char])
        elif char in close_brackets:
            # Check if stack has items AND the top item doesn't match the closing bracket
            if len(stack) == 0 or stack[-1] != char:
                return False
            stack.pop() # Remove the successfully matched closing bracket
            
    # If the stack is empty, all brackets were properly closed
    return len(stack) == 0

# --- Test Cases ---
print(is_balanced("{[()]}"))    # Output: True
print(is_balanced("{[(])}"))    # Output: False
print(is_balanced("(("))        # Output: False
print(is_balanced(""))          # Output: True
print(is_balanced("a(b)c"))     # Output: True
