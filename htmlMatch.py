def is_html_balanced(s:str) -> bool:
    tag_map = {'<div>':'</div>', '<p>':'</p>', '<span>':'</span>'}
    close_tags = set(tag_map.values())
    stack = []

    for tag in s:
        if tag in tag_map:
            stack.append(tag_map[tag])
        elif tag in close_tags:
            if len(stack) == 0 or stack[-1] != tag:
                return False
            stack.pop()
    return len(stack) == 0

print(is_html_balanced(['<div>', '<p>', '</p>', '</div>']))  # Output: True
print(is_html_balanced('<div id="sfcnt"></div>'))  # Output: True
