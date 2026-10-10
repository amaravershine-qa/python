def fibonacciSeries():
    n = int(input("Enter the limit till which you want to print the fibonacci series: "))
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    result = fib_series[:n]
    print(f"The fibonacci series upto {n} is: {result}")

fibonacciSeries()