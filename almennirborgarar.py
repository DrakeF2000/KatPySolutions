num_grills, people_waiting = map(int, input().split())
times_to_cook = sorted(list(map(int, input().split())))

def burgers_cooked(grills:list, time:int):
    burgers_cooked = 0
    for grill in grills:
        burgers_cooked += int(time // grill)
    return burgers_cooked

def binary_search( grills:list, target:int):
    lo, hi = -1, (times_to_cook[-1] * (target))

    while lo + 1 < hi:
        mid = int((lo + hi) // 2)
        if burgers_cooked(grills, mid) < target:
            lo = mid
        else:
            hi = mid
    return hi
print(binary_search( times_to_cook, (people_waiting + 1)))