import sys

problems, submit_count, attempts = [], [], []
total_time, problems_right = 0, 0
for line in sys.stdin:
    data = line.rstrip()
    if data == "-1":
        break
    else:
        temp = list(data.split())
        attempts.append(temp)
for i in range(len(attempts)):
    time, problem_letter, outcome = attempts[i]
    if problem_letter not in problems:
        problems.append(problem_letter)
        submit_count.append(0)
    if outcome == "wrong":
        submit_count[problems.index(problem_letter)] += 1
    elif outcome == "right":
        problems_right += 1
        total_time += (int(time) + (int(submit_count[problems.index(problem_letter)]) * 20))
print(f"{problems_right} {total_time}")