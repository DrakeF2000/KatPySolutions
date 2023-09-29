input()
data = list(map(int, input().split()))
data = data[::-1]
denominator, numerator = 1, 1
for i in range(len(data)):
    if i == 0:
        denominator = data[i]
    else:
        numerator += data[i] * denominator
        if i != len(data) - 1:
            denominator, numerator = numerator, denominator
print(f"{numerator}/{denominator}")