import math

f = open("2023/Advent2023-8.txt","r").read().split('\n')

instr = f[0].replace('L','0').replace('R','1')
maps = {}
ghost_pos = []

for line in f[2:]:
    maps[line[0:3]] = (line[7:10],line[12:15])
    if line[2] == 'A':
        ghost_pos.append(line[0:3])

#Part 1
result_1 = 0
cur_pos = 'AAA'
while cur_pos != 'ZZZ':
    for c in instr:
        result_1 += 1
        cur_pos = maps[cur_pos][int(c)]
        if cur_pos == 'ZZZ':break
print(result_1)

#Part 2
result_2 = 0
path_lengths = []

for g in ghost_pos:
    length = 0
    cur_pos = g
    while cur_pos[2] != 'Z':
        for c in instr:
            length += 1
            cur_pos = maps[cur_pos][int(c)]
            if cur_pos[2] == 'Z':break
    path_lengths.append(length)

print(path_lengths)
print(math.lcm(*path_lengths))