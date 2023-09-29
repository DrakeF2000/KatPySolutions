desired, receieved = list(input()), list(input())
for i in range(len(desired)):
    receieved.remove(desired[i])
duplicates = []
for i in range(len(receieved)):
    if receieved[i] not in duplicates:
        duplicates.append(receieved[i])
print("".join(duplicates))