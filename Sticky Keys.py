data = list(input())
output = []
for i in range(len(data)):
    if data[i] != data[i - 1]:
        output.append(data[i])
print("".join(output))