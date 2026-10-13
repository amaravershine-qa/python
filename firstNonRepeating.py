def find_first_uniques(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        print(char_count)
    for char in s:
        if char_count[char] == 1:
            return char
    return None
print(find_first_uniques("swiss"))
