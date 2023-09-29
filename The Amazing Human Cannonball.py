import math
test_cases = int(input())
output = []
for i in range(test_cases):
    initial_velocity, angle_from_ground, distance_to_wall, lower_wall_height, upper_wall_height = map(float, input().split())
    time_to_wall = distance_to_wall / (math.cos((angle_from_ground / 180 * math.pi)) * initial_velocity)
    height_at_wall = initial_velocity * time_to_wall * math.sin((angle_from_ground / 180 * math.pi)) - (0.5 * 9.81 * (time_to_wall ** 2))
    if height_at_wall > (lower_wall_height + 1) and height_at_wall < (upper_wall_height - 1):
        output.append("Safe")
    else:
        output.append("Not Safe")
for i in range(len(output)):
    print(output[i])    