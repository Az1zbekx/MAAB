def fun(arr1, arr2):
    arr3 = []
    for i in arr1:
        if i not in arr2:
            arr3.append(i)
    for i in arr2:
        if i not in arr1:
            arr3.append(i)
    return arr3
arr1 = list(map(str, input("1 - list: ").split()))
arr2 = list(map(str, input("2 - list: ").split()))
print(fun(arr1, arr2))