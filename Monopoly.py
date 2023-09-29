meh, odds, data, prob = input(), [1,2,3,4,5,6,5,4,3,2,1], list(map(int, input().split())), 0
for i in range(len(data)):
    multiplyer = odds[data[i] - 2]
    prob += (1/6) * (1/6) * odds[data[i] - 2]
print(prob)