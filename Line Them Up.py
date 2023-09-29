count = int(input())
data = []
for i in range(count):
    data.append(input())
alphabetical, reverse = sorted(data), sorted(data)[::-1]
if data == alphabetical:
    print("INCREASING")
elif data == reverse:
    print("DECREASING")
else:
    print("NEITHER")