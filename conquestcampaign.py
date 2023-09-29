rows, columns, weak_cells = map(int, input().split())
graph = [[0 for i in range(columns)] for j in range(rows)]
for i in range(weak_cells):
    row, column = map(int, input().split())
    graph[row - 1][column - 1] = 1

def safe(row, column):
    return 0 <= row < rows and 0 <= column < columns

def check_done(graph):
    for row in graph:
        if 0 in row:
            return False
    return True

dz = [(1, 0), (0, 1), (-1, 0), (0, -1)]
days = 1
while True:
    if check_done(graph) == True:
        print(days)
        break
    new_graph = [r[:] for r in graph]
    
    for row in range(rows):
        for column in range(columns):

            for move in dz:
                new_row, new_col = row + move[0], column + move[1]
                if safe(new_row, new_col) and graph[row][column] == 1:
                    new_graph[new_row][new_col] = 1
    graph = new_graph
    days += 1