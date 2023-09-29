percent = int(input())
print(f"{(1/(percent/100)):.10f}" + "\n" + f"{(1/(abs(100-percent)/100)):.10f}")
