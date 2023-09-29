output = []
while True:
    s, a, b, c = map(int, input().split())
    if s == 0 and a == 0 and b == 0 and c == 0:
        break
    else:
        output.append(( ((s - a + 40) % 40 + (b - a + 40) % 40 + (b - c + 40) % 40) * 9 ) + 1080)
for i in range(len(output)):
    print(output[i])