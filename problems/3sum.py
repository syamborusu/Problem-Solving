def threeSum(nums):
        n=len(nums)                #length of arry
        nums.sort()                #sort the array
        res=[]                     #empty resultant array to store the out put array
        for i in range(n-2):       # for loop run until n-2 element because "l" is i+1,"r" is n-1
            if i>0 and nums[i]==nums[i-1]:  #because if both the values is same then it leads to duplicate triplates
                continue      #skip the condition
            else:
                l=i+1                # "l" starts with i+1th index
                r=n-1                # "r" starts with last index n-1
                while l<r:           # while loop run until l<r
                    val=nums[i]+nums[l]+nums[r]   #assign the result to val  
                    if val==0:                   #if result of val is 0
                        res.append([nums[i],nums[l],nums[r]])     #then append to resultent array
                        l+=1                       # l+1 for next calculation 
                        while nums[l]==nums[l-1] and l<r:    # this condition used for to avoiod duplicate triplates
                            l+=1
                        while nums[r]==nums[r-1] and r<l:   # this condition used for to avoiod duplicate triplates
                            r-=1
                    elif val>0:           
                        r-=1
                    else:
                        l+=1
        return res
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums)) 