students = int(input())
data = []
for i in range(students):
    data.append(int(input()))
for i in range(1, 100000):
    working_set = []
    for j in range(len(data)):
        temp = data[j] % i
        if temp in working_set:
            break
        else:
            working_set.append(temp)
    if len(working_set) == len(data):
        print(i)
        break
