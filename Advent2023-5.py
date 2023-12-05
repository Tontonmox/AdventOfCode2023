#Returns the results corresponding to value v using map m
def get_value(v,m):
    r = 'none'
    for l in m:
        cur_map = [int(i) for i in l.split()]
        if int(v) in range(cur_map[1],cur_map[1] + cur_map[2]):
            r = str(int(v) + cur_map[0] - cur_map[1])
    
    if r == 'none':
        r = v

    return r

f = open("2023/Advent2023-5.txt","r").read().split('\n\n')

#Get seeds and maps from input
seeds = [s.strip() for s in f[0][6:].split()]

maps = []
for m in f[1:]:
    maps.append(m.split('\n')[1:])

results_1 = []
for s in seeds:
    v = s
    for m in maps:
        v = get_value(v,m)
    results_1.append(v)

print(min(results_1))
