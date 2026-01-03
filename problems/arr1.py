arr=[1,3,2]
arr2=[5,4,7,6]
total=arr+arr2
print(total)
total.sort()
print(total)
total.reverse()
print(total)
total1=total[::-1]
print("total1:",total1)
print("="*50)
target=11
for i in range(len(total1)):
    for j in range(i+1,len(total1)):
        if total1[i]+total1[j]==target:
            print(i,j)


