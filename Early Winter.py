years, snow_dm = map(int, input().split())
dms = list(map(int, input().split()))
count = 0
for i in range(len(dms)):
    if dms[i] <= snow_dm:
        print(f"It hadn't snowed this early in {i} years!")
        break
    else:
        count += 1
if count == len(dms):
    print("It had never snowed this early!")