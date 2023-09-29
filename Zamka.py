a, b, x = int(input()), int(input()), int(input())
data = []
for i in range(b + 1):
    if i >= a:
        temp = str(i)
        sum = 0
        for j in range(len(temp)):
            sum += int(temp[j])
        if sum == x:
            data.append(i)
print(f"{data[0]}\n{data[(len(data)) - 1]}")