def vowelCount():
    sum = 0
    str = input("Enter the string to count the number of vowels: ").lower()
    for char in str:
        if char in 'aeiou':
            sum+=1
    print(f"Number of vowels in string {str} is: {sum}")

vowelCount()