#Pair with given Sum (Two Sum)
def chkPair(A,size, x):
    for i in range(0, size - 1):  
        for j in range(i + 1, size):
            if (A[i] + A[j] == x):
                return 1
A = [4,-2,1,3]
x = 2
size = len(A)

if (chkPair(A,size, x)):
    print("Yes")

else:
    print("No")     
#Time Complexity: O(N2)
#Auxiliary Space: O(1)