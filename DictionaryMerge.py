def mergeDict():
    dict1 = {"a":"1", "b":"2", "c":"3"}
    dict2 = {"f":"6", "d":"4", "e":"5"}
    mergedDict = {**dict1,**dict2}
    print(f"The merged dictionary is: {mergedDict}")
mergeDict()