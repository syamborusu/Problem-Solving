def main(arr,n):  
        for i in range(0,n,2):
              if i>0 and arr[i]<arr[i-1]:
                arr[i],arr[i-1]=arr[i-1],arr[i]
                if i<n-1 and arr[i]<=arr[i+1]:
                    arr[i],arr[i+1]=arr[i+1],arr[i]
        return arr
arr=[10,5,6,3,2,20,100,80]
n=len(arr)
print(main(arr,n))
#tc=O(N/2)=O(N)==LINEAR
#sc=O(1)==constant space