sim_time, class_start, buses = map(int, input().split())
walk_times = list(map(int, input().split()))
bus_times = list(map(int, input().split()))
bus_intervals = list(map(int, input().split()))

for i in range(buses):
    sim_time += walk_times[i]
    if sim_time < bus_intervals[i]:
        time_to_wait = bus_intervals[i] - sim_time
    else:
        time_to_wait = sim_time % bus_intervals[i]
    if time_to_wait != 0:
        sim_time += time_to_wait
    sim_time += bus_times[i]
sim_time += walk_times[-1]
if sim_time <= class_start:
    print("yes")
else:
    print("no")