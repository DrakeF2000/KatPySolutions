nums = sorted(list(map(int, input().split())))
output = ""
data = list(input())
for i in range(len(data)):
    if data[i] == "A": output += str(nums[0]) + " "
    elif data[i] == "B": output += str(nums[1]) + " "
    elif data[i] == "C": output += str(nums[2]) + " "
print(output)
