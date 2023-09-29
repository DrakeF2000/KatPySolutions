import sys
output = []

def switch(n):
    if n % 2 == 1:
        return 9
    else:
        return 2

for line in sys.stdin:
    data = int(line.rstrip())
    if data == -1:
        break
    cur, moves = 1, 0
    while cur < data:
        moves += 1
        cur *= switch(moves)
    if moves % 2 == 1:
        output.append("Stan wins.")
    else:
        output.append("Ollie wins.")
for i in range(len(output)):
    print(output[i])