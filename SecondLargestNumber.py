def findSecondLargest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) >= 2 else None
result = findSecondLargest([1,4,23,54,11,3,3,4,2,5,66,54,87])
print(result)