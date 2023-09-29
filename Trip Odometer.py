input()
output = []
data = list(map(int, input().split()))
total = sum(data)
data = list(set(data))

for i in range(len(data)):
    temp = total - data[i]
    if temp not in output:
        output.append(temp)
print(len(output))
print(" ".join(sorted(list(map(str, output)))))