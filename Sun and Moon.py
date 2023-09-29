sun_last, sun_cycle = map(int, input().split())
moon_last, moon_cycle = map(int, input().split())

cur_sun = sun_cycle - sun_last 
cur_moon = moon_cycle - moon_last
for i in range(10000):
    if cur_moon == 0 and cur_sun == 0:
        print(i)
        break
    else:
        if cur_moon == 0:
            cur_moon = moon_cycle
        if cur_sun == 0:
            cur_sun = sun_cycle
        cur_sun -= 1
        cur_moon -= 1