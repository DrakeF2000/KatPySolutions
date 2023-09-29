data = list(input())
robust = 1
for i in range(len(data)):
    if data.count(data[i]) > 1:
        robust = 0
print(robust)
