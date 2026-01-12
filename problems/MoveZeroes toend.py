arr = [0, 1, 0, 3, 12]
pos = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos] = arr[i]
        pos += 1
while pos < len(arr):
    arr[pos] = 0
    pos += 1
print(arr)
#TC=O(N),SC=O(1)

#Brute force

arr = [0, 1, 0, 3, 12]
result = []
zero_count = 0
for num in arr:
    if num != 0:
        result.append(num)
    else:
        zero_count += 1
for _ in range(zero_count):
    result.append(0)
print(result)

#TC=O(N),SC=O(N)
