def listIntersection():
    list1 = [2,3,12,43,56,64]
    list2 = [2,3,5,65,76,87]
    result =[]
    i,j = 0,0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            i+=1
        elif list1[i] > list2[j]:
            j+=1
        else:
            result.append(list1[i])
            i+=1
            j+=1
    print(result)
listIntersection()