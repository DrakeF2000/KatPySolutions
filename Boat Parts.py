p, n = map(int, input().split())
replaced = []

for i in range(n):
    replaced.append(input())
done = []
for i in range(len(replaced)):
    if replaced[i] not in done:
        done.append(replaced[i])
    if len(done) == p:
        print(i + 1)
        break
if len(done) != p:
    print("paradox avoided")

