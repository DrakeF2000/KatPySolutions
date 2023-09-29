num_count, operator = map(int, input().split())
nums = list(map(int,input().split()))
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
if operator == 1:
    print(7)
elif operator == 2:
    if nums[0] > nums[1]:
        print("Bigger")
    elif nums[0] == nums[1]:
        print("Equal")
    else:
        print("Smaller")
elif operator == 3:
    print((sorted([nums[0], nums[1], nums[2]]))[1])
elif operator == 4:
    print(sum(nums))
elif operator == 5:
    total = [x for x in nums if x % 2 == 0]
    print(sum(total))
elif operator == 6:
    string = []
    for i in range(len(nums)):
        string.append(alphabet[nums[i] % 26])
    print("".join(string))
elif operator == 7:
    i = 0
    visited = set()
    while True:
        i = nums[i]
        if i < 0 or i > (len(nums) - 1):
            print("Out")
            break
        elif i == (len(nums) - 1):
            print("Done")
            break
        else:
            if i not in visited:
                visited.add(i)
            else:
                print("Cyclic")
                break