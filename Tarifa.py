meg_count, month_count = int(input()), int(input())
total = meg_count
for i in range(month_count):
    data = int(input())
    total += meg_count
    total -= data
print(total)