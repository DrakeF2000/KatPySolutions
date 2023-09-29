import sys
count = int(int(input()) // 2) + 1
data = {}

for i in range(count):
    a, b = map(int, sys.stdin.readline().strip().split())
    if a in data:
        data[a] += 1
    else:
        data[a] = 1
    if b in data:
        data[b] += 1
    else:
        data[b] = 1
out = []
for key, value in data.items():
    if value > 1:
        out.append(key)
if out[0] > out[1]:
    out[0], out[1] = out[1], out[0]
print(f"{out[0]} {out[1]}")