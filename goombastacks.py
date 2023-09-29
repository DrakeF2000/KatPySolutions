goombas, rooms = 0, int(input())
flag = True
for i in range(rooms):
    goomba_here, escape = map(int, input().split())
    goombas += goomba_here
    if goombas < escape:
        flag = False
if flag:
    print("possible")
else:
    print("impossible")