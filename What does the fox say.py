test_cases = int(input())
output = []

for i in range(test_cases):
    data = list(map(str, input().split()))
    noises = []
    while True:
        temp = input().split()
        if temp[0] == "what":
            break
        else:
            noises.append(temp[2])
    for noise in noises:
        if noise in noises:
            while noise in data:
                data.remove(noise)
    output.append(" ".join(data))
for i in range(len(output)):
    print(output[i])