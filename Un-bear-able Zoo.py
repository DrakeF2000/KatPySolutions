import sys

test_case = 1
for line in sys.stdin:
    animals = int(line.rstrip())
    if animals == 0:
        break
    data = {}
    for i in range(animals):
        animal_data = [word.lower() for word in input().split()]
        if animal_data[-1] in data:
            data[animal_data[-1]] += 1
        else:
            data[animal_data[-1]] = 1
    dict_keys = sorted(data.keys())
    sys.stdout.write(f"List {test_case}:\n")
    for key in dict_keys:
        sys.stdout.write(f"{key} | {data[key]}\n")
    test_case += 1