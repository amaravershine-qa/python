import math

def is_prime(n):
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
        
    # 2 is the only even prime number
    if n == 2:
        return True
        
    # Exclude all other even numbers
    if n % 2 == 0:
        return False
        
    # Check odd factors up to the square root of n
    # We step by 2 to skip even numbers
    square_root = int(math.isqrt(n))
    for i in range(3, square_root + 1, 2):
        if n % i == 0:
            return False
            
    return True
# Generating first 100 prime numbers
primes = []
current_number = 2
while len(primes) < 100:
    if is_prime(current_number):
        primes.append(current_number)
    current_number+=1
print(primes)

# Checking whether a number is prime or not
try:
# Prompt the user for input and convert it to an integer
    user_input = int(input("Enter a positive integer to check: "))

# Call the function and print the result
    if is_prime(user_input):
        print(f"✨ {user_input} is a prime number!")
    else:
        print(f"❌ {user_input} is not a prime number.")

except ValueError:
    print("Invalid input! Please enter a valid whole number.")

# Finding prime numbers in a list
lst = [1,2,3,7,43,12,34,65,89,91]
prime_list = []
for items in lst:
    if is_prime(items):
        prime_list.append(items)
print(f"The list of prime numbers is {prime_list}")

# Finding prime number in a range
start_point = int(input("Enter the starting point: "))
end_point = int(input("Enter the ending point: "))
prime_list_range = []
for items in range(start_point,end_point+1):
    if is_prime(items):
         prime_list_range.append(items)
print(f"prime numbers from {start_point} to {end_point} is: {prime_list_range}")

