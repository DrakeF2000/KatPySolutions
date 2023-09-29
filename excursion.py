data = list(map(int, list(input())))
non_zeros = 0

swap_count = 0
for i in range(len(data)):
    if data[i] == 0:
        swap_count += non_zeros
    else:
        non_zeros += 1

ones_in_the_way = 0
for i in reversed(range(len(data))):
    if data[i] == 2:
        swap_count += (ones_in_the_way)
    elif data[i] == 1:
        ones_in_the_way += 1
print(swap_count)