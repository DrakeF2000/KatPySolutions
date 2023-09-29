import sys
output = []

for line in sys.stdin:
    data = list(map(int, line.rstrip().split()))
    for i in range(len(data)):
        sum_of_others = 0
        for j in range(len(data)):
            if j != i:
                sum_of_others += data[j]
        if sum_of_others == data[i]:
            output.append(data[i])
            break
for i in range(len(output)):
    print(output[i])