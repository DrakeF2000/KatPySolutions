blocks = int(input())
temp, i, layers = 0, 1, 0
while temp <= blocks:
    temp += (i ** 2)
    i += 2
    layers += 1
print(layers - 1)