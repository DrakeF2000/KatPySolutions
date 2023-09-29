hand_count, dominant_suit = map(str, input().split())
cards_per_hand = 4
not_dominant = [11, 0, 0, 0, 0, 0, 0, 0, 0, 10, 2, 3, 4]
dominant = [11, 0, 0, 0, 0, 0, 0, 0, 14, 10, 20, 3, 4]
cards = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
data = []
for i in range(int(hand_count) * cards_per_hand):
    data.append(input())
total = 0
for i in range(len(data)):
    temp = data[i]
    card, suit = temp[0], temp[1]
    if suit != dominant_suit:
        total += not_dominant[cards.index(card)]
    else:
        total += dominant[cards.index(card)]
print(total)