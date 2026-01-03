#linear search 
def ls(list,target):
    for i in range(0,len(list)):  
        if list[i]==target:
            return i
    else:
        return "not in list"
list=[1,3,5,7,9,11]
target=5
print(ls(list,target))