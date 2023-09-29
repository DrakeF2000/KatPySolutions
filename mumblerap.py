a, data, window, nums = input(), list(input()), [], []
data.append("c")
for c in data:
    try: window.append(str(int(c)))
    except Exception:
        if len(window) > 0:
            nums.append(int("".join(window)))
            window = []
print(max(nums))