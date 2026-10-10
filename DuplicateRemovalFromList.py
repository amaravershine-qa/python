def duplicateRemoval(lst):
    resultantList = list(set(lst))
    print(f"The initial list is: {lst}")
    print(f"The vetted list is: {resultantList}")

duplicateRemoval([1,1,2,2,3,3,4,4,5,6,7,8,9,0,1,2,5,4,4,6,7])