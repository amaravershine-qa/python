def stringRotation():
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    if (len(s1) == len(s2)) and (s2 in (s1+s1)):
        print("True")
    else:
        print("False")
stringRotation()  

