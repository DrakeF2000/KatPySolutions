import sys
output = []
for line in sys.stdin:
    output.append(float(eval(line)))
for elem in output:
    print(f"{elem:.2f}")