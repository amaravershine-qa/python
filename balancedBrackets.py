def is_balanced(s:str) -> bool:
    bracket_map = {'{':'}', '(':')', '[':']'}
    close_bracket = set(bracket_map.values())
    stack = []
    for char in s:
        if char in bracket_map:
            stack.append(bracket_map[char])
        elif char in close_bracket:
            if len(stack) == 0 or stack[-1] != char:
                return False
            stack.pop()
    return(len(stack) == 0)
print(is_balanced("{[()]}"))    # Output: True

# Pytest parametrization with meaningful IDs
@pytest.mark.parametrize(
    "payload, expected",
    [
        # Perfectly Balanced Cases
        ("{[()]}", True),
        ("a(b)c", True),
        ("", True),
        ("{}", True),
        ("()[]{}", True),
        
        # Mismatched/Incorrect Order Cases
        ("{[(])}", False),
        ("(]", False),
        ("([)]", False),
        
        # Unclosed/Leftover Cases
        ("((", False),
        ("{[()", False),
        ("(", False),
        
        # Unexpected Closing Cases
        (")", False),
        ("]}", False),
        ("abc)", False),
    ],
    ids=[
        "valid_deeply_nested",
        "valid_mixed_text_and_brackets",
        "valid_empty_string",
        "valid_single_pair",
        "valid_consecutive_pairs",
        
        "invalid_wrong_nesting_order",
        "invalid_mismatched_pair_types",
        "invalid_interleaved_brackets",
        
        "invalid_multiple_unclosed",
        "invalid_incomplete_nesting",
        "invalid_single_unclosed",
        
        "invalid_starts_with_closing",
        "invalid_only_closing",
        "invalid_trailing_closing_bracket",
    ]
)
def test_is_balanced(payload, expected):
    assert is_balanced(payload) == expected