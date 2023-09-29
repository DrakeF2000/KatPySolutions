cur = 1
data = list(input())
for i in range(len(data)):
    if data[i] == "A":
        if cur == 1 or cur == 2:
            if cur == 2:
                cur = 1
            elif cur == 1:
                cur = 2
    elif data[i] == "B":
        if cur == 2 or cur == 3:
            if cur == 2:
                cur = 3
            elif cur == 3:
                cur = 2
    elif data[i] == "C":
        if cur == 1 or cur == 3:
            if cur == 1:
                cur = 3
            elif cur == 3:
                cur = 1
print(cur)