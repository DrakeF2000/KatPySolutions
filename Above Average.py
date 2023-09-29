testCount = int(input())
output = []
for i in range(testCount):
    data = list(map(int, input().split()))
    data.remove(data[0])
    avg = sum(data) / len(data)
    avgCount = 0
    for i in range(len(data)):
        if data[i] > avg:
            avgCount += 1
    percent = (avgCount / len(data)) * 100
    output.append('{:.3f}'.format(percent))
for i in range(len(output)):
    print(str(output[i]) + "%")