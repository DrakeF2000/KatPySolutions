test_cases = int(input())
output = []

for i in range(test_cases):
    gene_block_size = int(input())
    count = 0
    while True:
        if list(str(gene_block_size))[::-1][0] == "7":
            output.append(count + 1)
            break
        elif gene_block_size <= 0:
            output.append("-1")
            break
        else:
            count += 1
            gene_block_size -= 7 
for i in range(len(output)):
    print(output[i])