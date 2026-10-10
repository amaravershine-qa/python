def commonElements():
    lsst1 = [1,2,3,4,5,6,7,8,9,0]
    lsst2 = [1,2,3,4,5,6,7,8,9,0]
    result = list(set(lsst1) & set(lsst2))
    print(f"Common elements in both the lists is: {result}")

commonElements()