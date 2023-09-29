arr = [True for i in range(10)]

running = True
while running:
    num = int(input())
    if num == 0:
        break
    response = input()
    if response == "too low":
        for i in range(num):
            arr[i] = False
    elif response == "too high":
        for i in range(num - 1, 10):
            arr[i] = False
    else:
        if arr[num - 1]:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")
        arr = [True for i in range(10)]