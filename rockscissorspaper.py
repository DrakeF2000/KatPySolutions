import sys
input = sys.stdin.readline
test_cases = int(input().strip())

def safe(r, c, grid_r, grid_c): 
    return 0 <= r < grid_r and 0 <= c < grid_c  
dz = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def battle_win(challenger, opponent):
    if challenger == "P" and opponent == "R":
        return True
    if challenger == "R" and opponent == "S":
        return True
    if challenger == "S" and opponent == "P":
        return True
    return False

for i in range(test_cases):
    rows, columns, days = map(int, input().strip().split())
    graph = [list(input().strip()) for _ in range(rows)]

    for j in range(days):
        new_graph = [r[:] for r in graph]

        for row in range(rows):
            for column in range(columns):
                
                for move in dz:
                    new_row, new_column = row + move[0], column + move[1]
                    if safe(new_row, new_column, rows, columns) and battle_win(graph[row][column], graph[new_row][new_column]):
                        new_graph[new_row][new_column] = graph[row][column]
        graph = new_graph
    for row in graph:
        print("".join(row))