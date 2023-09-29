data, sum = input(), 0
for c in data:
    sum += ord(c)
print(chr(int(sum / len(data))))