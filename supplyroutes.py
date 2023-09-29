n, m, q = map(int, input().split())
graph = [set() for i in range(n)]
disjoint_set = [i for i in range(n)]
size = [1 for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)
qs = [tuple(map(int, input().split())) for i in range(q)]
for t, a, b in qs:
    if t == 0:
        # street overrun
        graph[a].remove(b)
        graph[b].remove(a)

def find(x):
    if disjoint_set[x] == x:
        return x
    disjoint_set[x] = find(disjoint_set[x])
    return disjoint_set[x]

def union(x, y):
    x, y = find(x), find(y)

    if x == y:
        return
    if size[x] < size[y]:
        x, y = y, x
    size[x] = size[x] + size[y]
    disjoint_set[y] = x

def initialize_disjoint_set(graph):
    for i in range(len(graph)):
        for node in graph[i]:
            union(i, node)

initialize_disjoint_set(graph)
qs = qs[::-1]
output = []
for t, a, b in qs:
    if t == 0:
        union(a, b)
    elif t == 1:
        output.append("safe" if find(a) == find(b) else "unsafe")
output = output[::-1]
for i in output:
    print(i)