import math
def calculateFactorial():
    number = int(input("Enter a number to calculate factorial: "))
    try:
        result = math.factorial(number)
        print(f"Factorial of {number} is {result}")
    except ValueError:
        print("The number cannot be negative")

calculateFactorial()
