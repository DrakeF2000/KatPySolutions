big, divide = map(int, input().split())
temp = big // divide
lo, hi = temp*divide, (temp+1)*divide
loDis, hiDis = abs(big - lo), abs(big-hi)
closest = min(loDis, hiDis)
print(closest)