from collections import Counter
def charCounter(str):
    sampleString = input("Enter a string to count the characters: ")
    result = dict(Counter(sampleString))
    print(f"The result of character count is: {result}")
charCounter()