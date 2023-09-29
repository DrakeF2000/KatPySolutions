total_judges, already_voted = map(int, input().split())
cur_score = 0
for i in range(already_voted):
    cur_score += int(input())
left_to_vote = total_judges - already_voted
minimum_score, maximum_score = (cur_score + (left_to_vote * -3)) / total_judges, (cur_score + (left_to_vote * 3)) / total_judges
print(minimum_score, maximum_score)