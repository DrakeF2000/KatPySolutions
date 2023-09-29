pizza_count, pizza_costs, total = int(input()), [], 0
for i in range(pizza_count):
    data = list(input().split())
    pizza_costs.append(int(data[1]))
pizza_costs = sorted(pizza_costs)[::-1]
for i in range(0, len(pizza_costs), 2):
    total += pizza_costs[i]
print(total)