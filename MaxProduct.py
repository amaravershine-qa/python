def maxProductIntegers():
    lst = [-5,-6,-8,-1,-3,-2,-1,-4,-7]
    lst.sort()
    result = max((lst[0]*lst[1]) , (lst[-1]*lst[-2]))
    print(f"The max product is: {result}")
maxProductIntegers()
