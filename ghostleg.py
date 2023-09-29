n, m = map(int, input().split())
p = [i + 1 for i in range(n)]
for i in range(m):
    b = int(input())
    a = b - 1
    p[a], p[b] = p[b], p[a]
for i in range(len(p)):
    print(p[i])