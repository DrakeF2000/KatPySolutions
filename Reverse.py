count = int(input())
output = []
for i in range(count):
    output.append(input())
output = output[::-1]
for i in range(len(output)):
    print(output[i])