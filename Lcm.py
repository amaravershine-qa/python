from math import gcd
def lcmCalculation():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    lcm = abs(num1 * num2) // gcd(num1 , num2)
    print(lcm)
lcmCalculation()