name, data = input(), [int(input()) for i in range(3)]
if data[0] - data[1] < 0 and data[2] > 0: print("SITH")
elif data[0] - data[1] == data[2] and data[2] < 0: print("JEDI")
else: print("VEIT EKKI")