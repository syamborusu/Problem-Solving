s="coder"
n=len(s)
for i in range(n):
    for j in range(i+1):
        print(s[i],end=' ')
    print()

print("================================")
s="coder"
n=len(s)
for i in range(n):
    for j in range(i+1):
        print(s[n-1-i],end=' ')
    print()