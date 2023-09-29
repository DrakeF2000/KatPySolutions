width, pieces = int(input()), int(input())
area = 0
for i in range(pieces):
    a, b = map(int, input().split())
    area += a * b
print(int(area / width))