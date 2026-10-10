def duplicateElement():
    seen = set()
    duplicate = set()
    lst = [1,2,2,4,5,6,6,7,8,9,2,3,1,5,3]
    for num in lst:
        if num in seen:
            duplicate.add(num)
        else:
            seen.add(num)
    duplicatedList = list(duplicate)
    print(duplicatedList)
duplicateElement()