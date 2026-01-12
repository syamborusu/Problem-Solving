def twosum(nums):
    dict1={}
    n=len(nums)
    for i in range(n):
        nums2=target-nums[i]
        if nums2 in dict1:
            return [dict1[nums2],i]
        else:
            dict1[nums[i]]=i
nums=[2,7,11,15]
target=22
print(twosum(nums))