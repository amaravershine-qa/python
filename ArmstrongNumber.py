def is_armstrong(n: int) -> bool:
    num_digits = 0
    temp = n
    while temp > 0:
        num_digits+=1
        temp//=10
    print(num_digits)

    temp = n
    sum_digits = 0
    while temp > 0:
        temp_digit = temp % 10
        sum_digits+= temp_digit ** num_digits
        temp//=10
    return sum_digits == n

print(is_armstrong(153))
