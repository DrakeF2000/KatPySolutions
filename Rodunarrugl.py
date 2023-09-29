_, arr, v, c = input(), [0] + list(map(int, input().split())), set(), 0
for i in range(1, len(arr)):
    if arr[i] in v:
        continue
    if arr[i] == i:
        v.add(arr[i])
    else:
        cur = arr[i]
        temp_v = set()
        while True:
            if cur in temp_v:
                c += len(temp_v) + 1
                break
            else:
                temp_v.add(cur)
                v.add(cur)
                cur = arr[cur]
print(c)