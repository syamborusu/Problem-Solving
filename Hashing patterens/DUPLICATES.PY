def duplicates(arr):
    dict={}
    for i in arr:
        if i in dict:
            return i, True
        else:
            dict[i]=1
    return False
arr=[1,2,4,3,3]
print(duplicates(arr))
