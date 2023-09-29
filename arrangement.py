roomCount = int(input())
peopleCount = int(input())

minPerRoom = int(peopleCount // roomCount)
peopleLeft = peopleCount - (minPerRoom * roomCount)

output = []
for i in range(roomCount):
    output.append("*" * minPerRoom)
for i in range(roomCount):
    temp = str(output[i])
    if peopleLeft >= 1:
        temp += "*"
        output[i] = temp
        peopleLeft -= 1
for i in range(len(output)):
    print(output[i])
    
