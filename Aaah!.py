produce = input()
required = input()

produceAs = produce.count('a')
requiredAs = required.count('a')

if requiredAs == 0 and produceAs == 0:
    if len(produce) >= len(required):
        print("go")
else:
    if produceAs >= requiredAs:
        print("go")
    else:
        print("no")