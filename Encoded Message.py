test_cases = int(input())
output = []
for i in range(test_cases):
    data = list(input())
    square = int(len(data) ** 0.5)
    build_arr = [[] for i in range(square)]
    for i in range(len(data)):
        loc = int(i % square)
        build_arr[loc].append(data[i])
    build_arr = build_arr[::-1]
    for i in range(len(build_arr)):
        build_arr[i] = "".join(build_arr[i])
    build_arr = "".join(build_arr)
    output.append(build_arr)
for i in range(len(output)):
    print(output[i])