def checkPalindrome():
    str = input("Enter a string to check for palindrome: ").lower()
    return str == str[::-1]

result = checkPalindrome()
print(result)