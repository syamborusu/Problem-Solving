def threeSum(nums):
        n=len(nums)
        nums.sort()
        res=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue      #skip the condition
            else:
                l=i+1
                r=n-1
                while l<r:
                    val=nums[i]+nums[l]+nums[r]
                    if val==0:
                        res.append([nums[i],nums[l],nums[r]])
                        l+=1
                        while nums[l]==nums[l-1] and l<r:
                            l+=1
                    elif val>0:
                        r-=1
                    else:
                        l+=1
        return res
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums)) 