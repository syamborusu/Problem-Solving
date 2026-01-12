a = "abcabbc"
seen = set()
l = 0
max_len = 0
for r in range(len(a)):
    while a[r] in seen:
        seen.remove(a[l])
        l += 1
    seen.add(a[r])
    max_len = max(max_len, r - l + 1)
print(max_len)
#tc=O(N)
#SC=O(N)



