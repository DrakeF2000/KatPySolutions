test_cases = int(input())
output = []
for j in range(test_cases):
    x, base, num = map(int, input().split())
    remainders = []
    while True:
        if num < base:
            remainders.append(num)
            break
        else:
            remain = num % base
            remainders.append(remain)
            num = int(num // base)
    total = 0
    for i in range(len(remainders)):
        total += remainders[i] ** 2
    output.append(f"{j + 1} {total}")
for i in range(len(output)):
    print(output[i])