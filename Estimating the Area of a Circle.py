import math
output = []
running = True
while running:
    radius, marked_points, in_circle = map(float,input().split())
    if radius == 0 and marked_points == 0 and in_circle == 0:
        break
    output.append(f"{radius ** 2 * math.pi} {4 * in_circle / marked_points * radius ** 2}")
for i in range(len(output)):
    print(output[i])