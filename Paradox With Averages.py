test_cases = int(input())
output = []

for i in range(test_cases):
    count = 0
    input()
    num_cs_students, num_eco_students = map(int, input().split())
    cs_students = sorted(list(map(int, input().split())))[::-1]
    eco_students = list(map(int, input().split()))
    average_cs_iq, average_eco_iq = sum(cs_students) / num_cs_students, sum(eco_students) / num_eco_students
    for i in range(len(cs_students)):
        if cs_students[i] > average_eco_iq and cs_students[i] < average_cs_iq:
            count += 1
        elif cs_students[i] < average_eco_iq:
                break
    print(count)