width, x_cut, y_cut = map(int, input().split())
print(max(width - x_cut, x_cut) * max(width - y_cut, y_cut) * 4)