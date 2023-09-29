rooms = int(input())
a, b, c = 0, 0, 0
binary_map = {"J": 1, "N":0}
for i in range(rooms):
    a1, b1, c1 = map(binary_map.get, input().split())
    a, b, c = a + a1, b + b1, c + c1
print(min(a, b, c))