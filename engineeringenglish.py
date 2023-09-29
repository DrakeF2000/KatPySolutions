import sys
words_used = []
for line in sys.stdin:
    data = list(line.strip().split())
    for word in data:
        if word.lower() not in words_used:
            sys.stdout.write(f"{word} ")
            words_used.append(word.lower())
        else:
            sys.stdout.write(". ")
    sys.stdout.write("\n")