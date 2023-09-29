memory = int(input())
line = list(input())

women, men = 0, 0
while len(line) != 0:
    if abs(women - men) + 1 > memory: # need to look at both the first and second person in line to keep balance
        if women > men:
            if line[0] == "M" or line[1] == "M":
                men += 1
                line.remove("M")
            else:
                break
        elif men > women:
            if line[0] == "W" or line[1] == "W":
                women += 1
                line.remove("W")
            else:
                break
    else: # just let them in, the difference is no problem
        if line[0] == "M":
            men += 1
            line.remove(line[0])
        elif line[0] == "W":
            women += 1
            line.remove(line[0])
print(men + women)