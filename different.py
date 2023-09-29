import sys
for line in sys.stdin:
    a, b = map(int, line.rstrip().split())
    sys.stdout.write(str(abs(a - b)) + "\n")