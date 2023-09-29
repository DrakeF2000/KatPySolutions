a, b = map(int, input().split())

if a % 2 == 1 and b % 2 == 1:
    print("impossible")
elif a % 2 == 1 and b % 2 == 0:
    print("possible")
elif a % 2 == 0 and b % 2 == 1:
    print("impossible")
else:
    print("possible")