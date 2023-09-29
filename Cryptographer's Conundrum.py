data = list(input())
base = "PER"

def difference(s1:str, s2:str):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count

i = 0
count = 0
while i < len(data) - 1:
    temp = f"{data[i]}{data[i + 1]}{data[i + 2]}"
    count += difference(temp, base)
    i += 3
print(count)