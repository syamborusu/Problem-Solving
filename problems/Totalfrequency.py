s = "aaabbac"
freq = {}   # Count frequency
for ch in s:
    freq[ch] = freq.get(ch,0) + 1   #if element found incress value by 1  
result = ""   #initiae empty result for str
seen = set()        
for ch in s:                          #ch = 'a'            
    if ch not in seen:                #'a' not in seen → ✅ True
        result += ch + str(freq[ch])  #result = "" + "a" + "4" → "a4"
        seen.add(ch)                  #seen = {'a'}
print(result)
#O(N) AND O(N)