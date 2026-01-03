def findMedianSortedArrays(nums1,nums2):
    fnums=nums1+nums2
    fnums.sort()  #sortedlist
    n=len(fnums)  #lenth of the list
    if n%2==1:     #if the length of the list is odd
        median=fnums[n//2]  #index of fnums is n//2
    else:
        median=(fnums[n//2-1]+fnums[n//2])/2.0
    return median #if the length of the list is even 
num1=[1,3,4]
num2=[2,6,5,7]
print(findMedianSortedArrays(num1,num2))