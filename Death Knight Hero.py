count, test_cases = 0, int(input())
for i in range(test_cases):
    data = input()
    if "CD" not in data:
        count += 1
print(count)