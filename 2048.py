board = []
for i in range(4):
    line = list(map(int, input().split()))
    board.append(line)
move = int(input())

def add_zeros(data:list, side):
    if side == 0: # left
        while len(data) != 4:
            data.insert(0, 0)
    elif side == 1: # right
        while len(data) != 4:
            data.append(0)

def rotate_matrix(board:list):
    temp_board = [[], [], [], []]
    for i in range(len(board)):
        line = board[i]
        for j in range(len(line)):
            temp_board[j].append(line[j])
    return temp_board

if move == 1 or move == 3:
    board = rotate_matrix(board)
# condense
for i in range(len(board)):
    line = board[i]
    while 0 in line:
        line.remove(0)
    if move == 2 or move == 3:
        line = line[::-1]
    j = 0
    while j < len(line) - 1:
        cur, next = line[j], line[j + 1]
        if cur == next:
            line[j] = cur *2
            line.remove(line[j + 1])
        j += 1
    if move == 2 or move == 3:
        line = line[::-1]
    # add zeros - make sure to adjust for correct move
    if move == 0 or move == 1:
        add_zeros(line, 1)
    elif move == 2 or move == 3:
        add_zeros(line, 0)
    board[i] = line
if move == 1 or move == 3:
    board = rotate_matrix(board)
for i in range(len(board)):
    print(" ".join(list(map(str, board[i]))))