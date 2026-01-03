def removeElement(nums,val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]  
            k += 1
    return k
nums = [1,2,3,1,5,1]
val = 1
k = removeElement(nums, val)
print("k =", k)                  
print("Modified nums =", nums[:k])