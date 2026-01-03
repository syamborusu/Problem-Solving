# twosum 
def twosum(nums,target):
    n=len(nums) 
    l=0
    r=n-1 
    while l<r:
        if nums[l] + nums[r] == target: 
            return [l,r]
        if nums[l] + nums[r]>target: 
            r-=1 
        else: 
            l+=1
    return "not found" 
nums=[0,2,7,11,15] 
target=17
print(twosum(nums,target))
#TC=O(n) #SC=O(1)
