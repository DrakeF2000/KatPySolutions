import sys
output = []

for line in sys.stdin:
    r, s = map(float, (line.rstrip()).split())
    if r == 0 and s == 0:
        break
    s += 0.16
    v = ((r * s) / 0.067) ** 0.5
    temp = int(v)
    temp2 = v - temp
    if temp2 > 0.5:
        output.append(temp + 1)
    else:
        output.append(temp)
for i in range(len(output)):
    print(output[i])