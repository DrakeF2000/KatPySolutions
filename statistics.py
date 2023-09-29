import sys
count = 1
for line in sys.stdin:
    data = list(map(int, line.strip().split()))
    data.remove(data[0])
    print(f"Case {count}: {min(data)} {max(data)} {max(data) - min(data)}")
    count += 1