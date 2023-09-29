word_count, job_count = map(int, input().split())
words = {}
output = []
for i in range(word_count):
    temp_data = list(input().split())
    words.update({f"{temp_data[0]}":int(temp_data[1])})
for i in range(job_count):
    data = []
    pay = 0
    collecting_job_data = True
    while collecting_job_data:
        temp = input()
        if temp == ".": 
            collecting_job_data = False
        else:
            temp = list(temp.split())
            for i in range(len(temp)):
                data.append(temp[i])
    for i in range(len(data)):
        if data[i] in words:
            pay += words[data[i]]
    output.append(pay)
for i in range(len(output)):
    print(output[i])