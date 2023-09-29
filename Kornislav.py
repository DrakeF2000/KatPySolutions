import itertools
lengths = list(map(int, input().split()))

def check_rect(walks, maxArea):
    x, y = 0, 0
    for i in range(len(walks)):
        if i == 0:
            x += walks[i]
        elif i == 1:
            y += walks[i]
        elif i == 2:
            x -= walks[i]
        elif i == 3:
            y -= walks[i]
    if x >= 0 and y <= 0:
        if x == 0:
            area = walks[0] * walks[1]
        else:
            area = (walks[3] + y) * (walks[0] - x)
        if area >= maxArea:
            return area
        else:
            return -1
    else:
        return - 1
    
maxArea = 0
for subset in itertools.permutations(lengths):
    temp = check_rect(subset, maxArea)
    if temp >= maxArea:
        maxArea = temp
print(maxArea)