from collections import deque
import heapq
import sys
input = sys.stdin.readline
# data input
R, C = map(int, input().strip().split())
grid = [input().strip() for _ in range(R)]

# tree distance matrix to be updated by bfs
tdist = [[None]*C for _ in range(R)] # RxC grid for tree distances

# to make sure moves are in bounds of matrix
dz = [(1,0),(-1,0),(0,1),(0,-1)] # manhattan moves
def safe(r,c): 
    return 0 <= r < R and 0 <= c < C

# finding the trees and sink/source
trees = []
for r in range(R):
    for c in range(C):
        if grid[r][c]=='+': trees.append((0,r,c))
        if grid[r][c]=='V': start = r,c
        if grid[r][c]=='J': end = r,c

#bfs
q, marked = deque(trees), set()
while len(q) > 0:
    d, r, c = q.popleft()    
    if (r,c) in marked: 
        continue
    tdist[r][c] = d
    marked.add((r, c))
    for dx, dy in dz:  #for up down left right
        x, y = dx+r, dy+c   #x and y = the new cell
        if safe(x, y):
            q.append((d + 1, x, y))

# run dijkstra's on the tdist matrix and store the min value
def dijkstras(tdist, row, column):
    pq = []
    heapq.heappush(pq, (-tdist[row][column], row, column))
    visited = set()

    while pq:
        tree_d, row, column = heapq.heappop(pq)

        if (row, column) in visited:
            continue
        
        if (row, column) == end:
            return -max(tree_d, -tdist[row][column])
        visited.add((row, column))


        for dx, dy in dz:
            move_row, move_column = row + dx, column + dy

            if safe(move_row, move_column) and (move_row, move_column) not in visited:
                heapq.heappush(pq, (max(-tdist[move_row][move_column], tree_d), move_row, move_column))
        
print(dijkstras(tdist, start[0], start[1]))