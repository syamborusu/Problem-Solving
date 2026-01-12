def duplicates(arr):
    dict={}
    for i in arr:
        if i in dict:
            return True
        else:
            dict[i]=1
    return False
arr=[1,2,4,3]
print(duplicates(arr))
