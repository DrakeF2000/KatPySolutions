matches, width, height = map(int, input().split())
max_length = ((width ** 2) + (height ** 2)) ** 0.5
for i in range(matches):
    temp = int(input())
    if temp <= max_length:
        print("DA")
    else:
        print("NE")