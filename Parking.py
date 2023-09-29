testCaseCount = int(input())
output = []
for i in range(testCaseCount):
    input()
    stores = list(map(int, input().split()))
    stores = sorted(stores)
    distance = (abs(stores[0] - stores[len(stores) - 1])) * 2
    output.append(distance)
for i in range(len(output)):
    print(output[i])