input()
data = sorted(list(map(int, input().split())))
score = 0
for i in range(len(data)):
    if data[i - 1] == data[i] - 1:
        pass
    else:
        score += data[i]
print(score)