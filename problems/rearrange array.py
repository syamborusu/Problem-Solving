def main(arr,n):
    x=1
    for i in range(1,n):
        if arr[i]!=arr[i-1]:
            arr[x]=arr[i]
            x+=1
    return arr[:x]
arr=[1,2,2,3,3,4,4,4,5,5]
n=len(arr)
print(main(arr,n))