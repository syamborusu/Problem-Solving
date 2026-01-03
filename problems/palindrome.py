def palindrome(s):
    n=len(s)
    l=0
    r=n-1
    while l<=r:
        if s[l]==s[r]:
            l+=1
            r-=1
        else:
            return False
    return True
s="racerar"
print(palindrome(s))