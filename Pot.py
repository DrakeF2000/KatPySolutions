numCount = int(input()) 
sum = 0
for i in range(numCount):
    num = input()
    num = num[::-1]
    expon = num[0]
    num = num[1:len(num)]
    num = num[::-1]
    sum += int(num) ** int(expon)
print(sum)