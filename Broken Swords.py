sword_count = int(input())

def binary_inverse(data:list):
    temp = []
    for i in range(len(data)):
        if data[i] == 0: temp.append(1)
        else: temp.append(0)
    return temp

sides, edges = 0, 0
for i in range(sword_count):
    t, b, l, r = map(int, binary_inverse(list(map(int, list(input())))))
    sides += (t + b)
    edges += (l + r)
print(f'{min(sides // 2, edges // 2)} {sides - min(sides // 2, edges // 2) * 2} {edges - min(sides // 2, edges // 2) * 2}')