output = []
run = True
while run:
    h, t = map(int, input().split())
    if h == 0 and t == 0:
        run = False
    moveCount = 0
    if h == 1 and t == 0:
        output.append("-1")
    else:
        if t % 2 == 1:
            t += 1
            moveCount += 1
        if (h + t / 2) % 2 == 1:
            moveCount += 2
            t += 2
        h += t / 2
        moveCount += t /2
        t = 0
        moveCount += h /2
        h = 0
        output.append(int(moveCount))
for i in range(len(output) - 1):
    print(output[i])