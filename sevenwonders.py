cards = list(input())
points = (cards.count("T") ** 2) + (cards.count("C") **2) + (cards.count("G") ** 2)
T, C, G = cards.count("T"), cards.count("C"), cards.count("G")
while T > 0 and C > 0 and G > 0:
    points += 7
    T, C, G = T - 1, C - 1, G - 1
print(points)