M = "m1"
W = ["w1", "w2", "w3"]

output = []

for i in range(len(W)):
    for j in range(i + 1, len(W)):
        output.append([M, W[i], W[j]])

print(output)
print(len(output))