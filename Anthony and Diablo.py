import math
a, b = map(float, input().split())
if (b**2)/(4 *math.pi) >= a:
    print("Diablo is happy!")
else:
    print("Need more materials!")