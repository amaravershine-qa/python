def rotate_string_left(text, n=3):
    """Rotates the string to the left by n positions."""
    # Handle shifts larger than the string length using modulo
    if not text:
        return text
    n = n % len(text)
    return text[n:] + text[:n]

def rotate_string_right(text, n=3):
    """Rotates the string to the right by n positions."""
    if not text:
        return text
    n = n % len(text)
    return text[-n:] + text[:-n]

# Example usage:
original_str = "Python"

left_rotated = rotate_string_left(original_str, 3)
right_rotated = rotate_string_right(original_str, 3)

print(f"Original:      '{original_str}'")
print(f"Left by 3:     '{left_rotated}'")   # "honPyt"
print(f"Right by 3:    '{right_rotated}'")  # "honPyt" (Note: "Python" has length 6, so a shift of 3 left or right ends up looking the same!)

# Example with a different word length to clearly show the difference:
word = "HelloWorld"
print(f"\nOriginal:      '{word}'")
print(f"Left by 3:     '{rotate_string_left(word, 3)}'")   # "loWorldHel"
print(f"Right by 3:    '{rotate_string_right(word, 3)}'")  # "rldHelloWo"
