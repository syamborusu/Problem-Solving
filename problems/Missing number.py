arr = [0, 1, 3]
n = 3
total = n * (n + 1) // 2
arr_sum = sum(arr)
print(total - arr_sum)

#TC=O(N)
#SC=O(N)

#Brute force
arr = [0, 1, 3]
n = 3
total = 0
for i in range(n + 1):
    total += i
arr_sum = 0
for num in arr:
    arr_sum += num

print(total - arr_sum)

#O(n),O(1)

