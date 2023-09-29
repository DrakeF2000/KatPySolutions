l, s = map(int, input().split())
data, i = list(map(int, input().split())), s - 1 
out = []
while i < len(data):
    out.append(data[i])
    i += s
print(" ".join(list(map(str, out))))