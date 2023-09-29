import itertools
def merge(build:list, operators:list):
    output = ""
    for i in range(len(build)):
        output += build[i]
        if i == len(build) - 1:
            break
        else:
            output += operators[i]
    return output

test_cases = int(input())
output = []

build = ['4','4','4','4']
equations = []
results = []
operators = ["+","-","*","//"]

for v in itertools.product(operators, repeat=3):
    test = merge(build, v)
    equals = eval(test)
    if "//" in test:
        while "//" in test:
                test = test.replace("//", "/")
                temp = " ".join(list(test))
                temp += f" = {equals}"
                equations.append(temp)
    else:
        temp = " ".join(list(test))
        temp += f" = {equals}"
        equations.append(temp)
    results.append(equals)
for i in range(test_cases):
    target = int(input())
    if target in results:
        location = results.index(target)
        output.append(equations[location])
    else:
        output.append("no solution")
for i in range(len(output)):
    print(output[i])