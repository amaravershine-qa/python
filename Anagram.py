def anagramCheck():
    s1 = input("Enter first string: ").lower()
    s2 = input("Enter the second string: ").lower()
    sorteds1 = sorted(s1)
    sorteds2 = sorted(s2)
    if sorteds1 == sorteds2:
        print(f"Strings {s1} and {s2} are anagrams")
    else:
        print(f"Strings {s1} and {s2} are not anagrams")
anagramCheck()