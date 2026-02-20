arr = [0, 1, 0, 3, 12]
pos = 0                   #posistion is intialize to 0th index
for i in range(len(arr)):        #loop starts from 0 to last index of arr
    if arr[i] != 0:              #0th index i not equal to 0
        arr[pos] = arr[i]        # pos is assigend with i th value
        pos += 1                 #Pos increment by 1 posistion ex:pos=1th index
while pos < len(arr):            #loop runs from value of pos to len of arr
    arr[pos] = 0                 #pos value is reassigend with zero
    pos += 1                     #pos will increment by 1 untill last element
print(arr)
#TC=O(N),SC=O(1)

#better optimal sol
nums= [0, 1, 0, 3, 12]
l = 0
for r in range(len(nums)):
    if nums[r] != 0:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
print(nums)


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
