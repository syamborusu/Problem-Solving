input = [2, 4, 1, 2, 1, 3]
freq = {}    #initialized empty dict
output = []   
for num in input:
    freq[num] = freq.get(num, 0) + 1  #If num exists, return its value or If num does not exist, return 0
for num in input:
    if freq[num] == 1:    #checks num in freq
        output.append(num)
print(output)

#TC=O(n) #SC=O(n)


#=================================
#Brute force

input = [2, 4, 1, 2, 1, 3]
output = []

for i in range(len(input)): 
    count = 0
    for j in range(len(input)):
        if input[i] == input[j]:
            count += 1
    if count == 1:
        output.append(input[i])
print(output)
#TC=O(N^2)
#SC=O(1)