import sys
sys.setrecursionlimit(1000000)
rs, cs, _ = map(int, input().split())
ws, g = list(map(int, input().split())), [list(input()) for i in range(rs)]
def f(r, c):
    if 0 <= r < rs and 0 <= c < cs:
        if g[r][c] == "O":
            g[r][c] = "~"
            f(r + 1, c)
        elif g[r][c] == "#" or g[r][c] == "?":
                if g[r - 1][c] == "~":
                    f(r - 1, c + 1)
                    f(r - 1, c - 1)
for w in ws:
    f(0, w)
for r in g:
    print("".join(r))