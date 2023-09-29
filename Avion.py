import sys
output = []
i = 1
for line in sys.stdin:
    if "FBI" in line.rstrip():
        output.append(i)
    i += 1
if len(output) == 0:
    print("HE GOT AWAY!")
else:
    for i in range(len(output)):
        print(output[i])