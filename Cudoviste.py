rows, columns = map(int, input().split())
cars_sqaushed = [0 for i in range(5)]
data = []
for i in range(rows):
    data.append((list(input())))
for i in range(rows - 1):
    for j in range(columns - 1):
        window = [data[i][j], data[i][j + 1], data[i + 1][j] , data[i + 1][j + 1]]
        if "#" not in window:
            crushed = int(window.count("X"))
            cars_sqaushed[crushed] += 1
for i in range(len(cars_sqaushed)):
    print(cars_sqaushed[i])