problem_count, test_cases = map(int, input().split())
passed_problems = 0

def check_pass(s):
    length = len(s)
    count = 0
    for i in range(len(s)):
        if s[i].islower():
            count += 1
    if count == length:
        return True
    else:
        return False

for i in range(problem_count):
    test_cases_passed = 0
    for j in range(test_cases):
        test_string = list(input())
        test_string.remove(test_string[0])
        if check_pass(test_string):
            test_cases_passed += 1
    if test_cases_passed == test_cases:
        passed_problems += 1
print(passed_problems)