bad_letters, data = list(input()), list(input().split())
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] in bad_letters:
            data[i] = "*" * len(data[i])
print(" ".join(data))