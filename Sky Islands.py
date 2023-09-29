island_count, bridge_count = map(int, input().split())
graph = []
for i in range(island_count + 1):
    graph.append([])
for i in range(bridge_count):
    a, b = map(int, input().split())
    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)
visited = []
for i in range(1, len(graph)):
    temp = graph[i]
    if len(visited) == 0:
        visited.append(i)
        for i in range(len(temp)):
            visited.append(temp[i])
    else:
        if i in visited:
            for i in range(len(temp)):
                if temp[i] not in visited:
                    visited.append(temp[i])
        else:
            for i in range(len(temp)):
                if temp[i] in visited:
                    for i in range(len(temp)):
                        if temp[i] not in visited:
                            visited.append(temp[i])
if len(visited) == island_count:
    print("YES")
else:
    print("NO")