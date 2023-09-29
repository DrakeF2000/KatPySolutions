test_cases, output = int(input()), []

for i in range(test_cases):
    input()
    data = list(map(int, input().split()))
    for j in range(len(data)):
        if data.count(data[j]) == 1:
            output.append(f"Case #{i + 1}: {data[j]}")
            break
for i in range(len(output)):
    print(output[i])