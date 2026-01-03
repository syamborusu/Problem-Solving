#Hash map approach
def longestConsecutive(nums):
    if not nums:
        return 0
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:   # start of sequence
            current = num
            count = 1
            while current + 1 in num_set:
                current += 1
                count += 1
            if count > longest:
               longest = count
    return longest
nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))
#TC=O(N)
#SC=O(N)

#===============================================

#Brute force approach
def longestConsecutive(nums):
    n = len(nums)
    longest = 0
    for i in range(n):
        current = nums[i]
        count = 1
        while current + 1 in nums:
            current += 1
            count += 1
        longest = max(longest, count)
    return longest
nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))
#TC=O(N^2)
#SC=O(N)

