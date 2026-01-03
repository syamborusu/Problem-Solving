def lcp(strs):
    if not strs:
        return "Noinput"
    pre=strs[0]        # Take the first string as the base prefix 
    for i in range(len(pre)):
        chr=pre[i]      # Take character by character from the first string
        for j in strs[1:]:  # Compare with all other strings
            if i>len(j) or j[i]!=chr:
                return pre[:i]# If mismatch or string too short, return prefix up to i
    return pre             # If no mismatch found, return the full first string
strs=["flower","flow","floght"]
print(lcp(strs))