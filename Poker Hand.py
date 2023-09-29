cards, score = list(card[0] for card in input().split()), 0
for i in range(len(cards)):
    score = max(score, cards.count(cards[i]))
print(score)