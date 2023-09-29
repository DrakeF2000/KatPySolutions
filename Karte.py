data, p, k, h, t = input(), 13, 13, 13, 13

duplicate = False
for i in range(0, len(data), 3):
    card_data = data[i:i+3]
    if data.count(card_data) > 1:
        print("GRESKA")
        duplicate = True
        break
    else:
        if card_data[0] == "P":
            p -= 1
        elif card_data[0] == "K":
            k -= 1
        elif card_data[0] == "H":
            h -= 1
        elif card_data[0] == "T":
            t -= 1
if duplicate == False:
    print(f"{p} {k} {h} {t}")