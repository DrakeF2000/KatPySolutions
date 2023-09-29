run = True
set = 1
output = []
while run:
    caseCount = int(input())
    if caseCount == 0:
        run = False
    else:
        top = []
        bottom = []
        for i in range(caseCount):
            if i % 2 == 1:
                bottom.append(input())
            else: top.append(input())
        bottom.reverse()
        for i in range(len(bottom)): top.append(bottom[i])
        output.append(f"Set {set}")
        set += 1
        for i in range(len(top)):
            output.append(top[i])
for i in range(len(output)):
    print(output[i])