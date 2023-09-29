import sys
output = []
for line in sys.stdin:
    data = list(map(int ,line.rstrip().split()))
    output.append(abs(data[0] - data[1]))
for i in range(len(output)):
    print(output[i])