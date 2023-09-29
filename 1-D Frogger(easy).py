arr_length, start_index, target_number = map(int, input().split())
arr = list(map(int, input().split()))

sim = True
hops = -1
start_index -= 1
visited = []
frog_index = start_index
while sim:
    hops += 1
    if frog_index < 0:
        print("left")
        print(hops)
        break
    if frog_index >= len(arr):
        print("right")
        print(hops)
        break
    if frog_index in visited:
        print("cycle")
        print(hops)
        break
    else:
        visited.append(frog_index)
    if arr[frog_index] == target_number:
        print("magic")
        print(hops)
        break
    elif arr[frog_index] > 0:
        frog_index += arr[frog_index]
    else:
        frog_index = frog_index - (abs(arr[frog_index]))