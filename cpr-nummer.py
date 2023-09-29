dob, id = map(str, input().split("-"))
data = list(dob + id)
multiply = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
total = 0
for i in range(len(data)):
    total += int(data[i]) * multiply[i]
if total % 11 == 0:
    print("1")
else:
    print("0")