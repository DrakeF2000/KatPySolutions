N, a = int(input()), []
for i in range(N): a.append([int(x) for x in input().split()[1::]])
o = [None] * (N + 1) 
def d(h, v):
    if h is None: return True
    if h in v: return False
    v.add(h)
    for n in a[h]: 
        if (d(o[n], v)): o[n] = h; return True
    return False
for i in range(N):
    if not d(i, set()): print("Neibb"); exit()
print(" ".join([str(x + 1) for x in o[1::]]))