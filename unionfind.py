import sys
input = sys.stdin.readline
n, q = map(int, input().split())
parents = [i for i in range(n)]
size = [1 for i in range(n)]

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x, y = find(x), find(y)

    if x == y:
        return
    if size[x] < size[y]:
        x, y = y, x
    size[x] = size[x] + size[y]
    parents[y] = x

for i in range(q):
    data = list(map(str, input().strip().split()))
    if data[0] == "=":
        union(int(data[1]), int(data[2]))
    elif data[0] == "?":
        print("yes" if find(int(data[1])) == find(int(data[2])) else "no")