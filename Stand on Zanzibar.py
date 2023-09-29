test_cases = int(input())
output = []
for i in range(test_cases):
    data = list(map(int, input().split()))
    imported = 0
    for i in range(len(data) - 1):
        if data[i + 1] > (data[i] * 2):
            imported += data[i + 1] - (data[i] * 2)
    output.append(imported)
for i in range(len(output)):
    print(output[i])