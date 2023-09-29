def recursive_factorial(n, product):
    if n == 1:
        return product
    else:
        return recursive_factorial(n - 1, product * n)

test_cases = int(input())
output = []
for i in range(test_cases):
    value = int(input())
    output.append((str(recursive_factorial(value, 1))[::-1])[0])
for i in range(len(output)):
    print(output[i])