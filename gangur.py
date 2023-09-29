data, total, to_be_passed = input(), 0, 0
for c in data:
    if c == ">":
        to_be_passed += 1
    elif c == "<":
        total += to_be_passed
print(total)