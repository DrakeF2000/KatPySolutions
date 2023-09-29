presses = int(input())
data = []
for i in range(presses):
    data.append(int(input()))
if len(data) % 2 == 1:
    print("still running")
else:
    total, i = 0, 0
    while i < len(data):
        first, second = data[i], data[i + 1]
        total += abs(second - first)
        i += 2
    print(total)
