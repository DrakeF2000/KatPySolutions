data = input()
if ":))" in data:
    print("double agent")
elif ":)" in data and ":(" in data:
    print("double agent")
elif ":)" in data:
    print("alive")
elif ":(" in data:
    print("undead")
else:
    print("machine")