h, m = map(int, input().split())
minutes = ((h * 60) + m) - 45
if minutes < 0:
    minutes += (24 * 60)
hours = minutes // 60
minute = minutes - (hours * 60)
print(f"{hours} {minute}")