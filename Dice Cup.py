d1, d2 = map(int, input().split())
data = []
output = []
for i in range(1, d1 + 1):
    for j in range(1, d2 + 1):
        temp = i + j
        data.append(temp)
data = sorted(data)
roll_counts = []
for i in range(1, d1 + d2):
    roll_counts.append(data.count(i))
most_rolls = max(roll_counts)
for i in range(len(roll_counts)):
    if roll_counts[i] == most_rolls:
        output.append(i + 1)
for i in range(len(output)):
    print(output[i])