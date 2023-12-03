import re
import string

#Return all 'symbols' adjacent to a given number
#Input has 3 args : number value, x position, y position
def adj_sym(n):
    x_min = max(0,n[2] - 1)
    x_max = min(n[2] + len(n[0]),l)
    y_min = max(0,n[1] -1)
    y_max = min(n[1] + 1,h)
    chars = [schem[y][x] for x in range(x_min,x_max+1) for y in range(y_min,y_max+1) if schem[y][x] not in string.digits + '.']
    return chars

#Return all numbers adjacent to a given gear
#Input is the x,y gear position
def find_adj_num(g):
    adj_num = [n[0] for n in numlist if (g[1] -1 <= n[1] <= g[1] + 1) and n[2] - 1<= g[0] <= n[2] + len(n[0]) ]
    return adj_num

f = open("2023/Advent2023-3.txt","r").read().split('\n')

#Processing inputs
schem = []
numlist = []
maybe_gear = []
for i,line in enumerate(f):
    schem.append(line)
    res = re.finditer(r'\d+',line)
    for r in res:
        numlist.append((r.group(0), i,r.start(0)))
    for j,c in enumerate(line):
        if c == '*':
            maybe_gear.append((j,i))
l = len(schem[0]) -1
h = len(schem) - 1

#Part 1 result
result_1 = 0
for n in numlist:
    if len(adj_sym(n)) > 0:
        result_1 += int(n[0])
print(result_1)

#Part 2 result
result_2 = 0
for g in maybe_gear:
    adj_num = find_adj_num(g)
    if len(adj_num) == 2:
        result_2 += int(adj_num[0]) * int(adj_num[1])
    
print(result_2)
