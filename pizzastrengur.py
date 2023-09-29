import sys
import random
main = ["P", "I", "Z", "A"]
guess = []

def make_copy(list_to_copy:list):
    return_list = []
    for c in list_to_copy:
        return_list.append(c)
    return return_list

test_set = make_copy(main)

word_count = int(input())
next_c = random.choice(test_set)
test_set.remove(next_c)
guess.append(next_c)
print("".join(guess), flush = True)
response = int(input())

while response != 2:
    if response == 1: # continue on, correct char
        test_set = make_copy(main)
        next_c = random.choice(test_set)
        test_set.remove(next_c)
        guess.append(next_c)
    elif response == 0: # incorrect guess
        guess = guess[:-1]
        next_c = random.choice(test_set)
        test_set.remove(next_c)
        guess.append(next_c)
        if len(test_set) == 0 and len(guess) <= word_count - 1:
            test_set = make_copy(main)
            next_c = random.choice(test_set)
            test_set.remove(next_c)
            guess.append(next_c)
    print("".join(guess), flush = True)
    response = int(input())