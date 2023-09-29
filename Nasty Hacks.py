test_cases = int(input())
output = []
for i in range(test_cases):
    ER_no_advertise, ER_advertise, cost_ad = map(int, input().split())
    if ER_no_advertise + cost_ad < ER_advertise:
        output.append("advertise")
    elif ER_no_advertise + cost_ad == ER_advertise:
        output.append("does not matter")
    else:
        output.append("do not advertise")
for i in range(len(output)):
    print(output[i])