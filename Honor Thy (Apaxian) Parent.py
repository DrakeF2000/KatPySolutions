first, last = map(list, input().split())
vowels = ["a", "i", "o", "u"]

if first[len(first) - 1] == "x" and first[len(first) - 2] == "e":
    temp = "".join(first) + "".join(last)
elif first[len(first) - 1] in vowels:
    temp = "".join(first[:-1]) + "ex" + "".join(last)
elif first[len(first) - 1] == "e":
    temp = "".join(first) + "x" + "".join(last)
else:
    temp = "".join(first) + "ex" + "".join(last)
print(temp)