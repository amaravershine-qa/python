def find_missing_num(nums,n):
    expected_sum = n * (n+1)//2
    actual_sum = sum(nums)
    return expected_sum-actual_sum

print(find_missing_num([1,2,3,4,6],6))