capacity, events = map(int, input().split())
count, cur = 0, 0
for i in range(events):
    action, amount = map(str, input().split())
    if action == "enter":
        if (cur + int(amount)) > capacity:
            count += 1
        else:
            cur += int(amount)
    elif action == "leave":
        cur -= int(amount)
print(count)