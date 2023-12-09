f = open("2023/Advent2023-9.txt","r").read().split('\n')

reports = []
for line in f:
    reports.append([int(c) for c in line.split()])

results_1 = []
results_2 = []

for r in reports:
    sequences = [r]
    
    while True:
        cur_s = sequences[-1]
        new_s = []
        for i in range(len(cur_s) -1):
            new_s.append(cur_s[i+1] - cur_s[i])
        
        sequences.append(new_s)
        if sum([1 for s in new_s if s != 0]) == 0:break
    
    #Saving the sequences before part 1 modifications
    seq_2 = sequences.copy()    

    #Part 1 solving
    for i in range(len(sequences)-2,-1,-1):
        sequences[i].append(sequences[i][-1] +  sequences[i+1][-1])
    
    results_1.append(sequences[0][-1])

    #Part 2 solving
    for i in range(len(seq_2)-2,-1,-1):
        seq_2[i] = [seq_2[i][0] - seq_2[i+1][0]] + seq_2[i]

    results_2.append(seq_2[0][0])

print(sum(results_1))
print(sum(results_2))