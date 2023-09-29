cur_wind, roads = int(input()), int(input())
for i in range(roads):
    road, safe_speed = map(str, input().split())
    if int(safe_speed) < cur_wind:
        print(road + " lokud")
    else:
        print(road + " opin")