from collections import deque

#Returns the results corresponding to value v using map m
def get_value(v,m):
    r = 'none'
    for l in m:
        cur_map = [int(i) for i in l.split()]
        if int(v) in range(cur_map[1],cur_map[1] + cur_map[2]):
            r = str(int(v) + cur_map[0] - cur_map[1])
            break
    
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
for i,s in enumerate(seeds):
    v = s
    for m in maps:
        v = get_value(v,m)
    results_1.append(int(v))


print(min(results_1))

next_test = []
for i in range(0,len(seeds),2):
    next_test.append((int(seeds[i]),int(seeds[i])+ int(seeds[i+1])-1))

to_test = deque(next_test)
next_test = []

for m in maps:
    for r in m:
        remains = []
        args = [int(a) for a in r.split()]
        while to_test:
            #Test range inside
            offset = args[0] - args[1]
            if (args[1] <= to_test[0][0] <= args[1] + args[2]) and (args[1] <= to_test[0][1] <= args[1] + args[2] - 1):
                next_test.append((to_test[0][0] + offset,to_test[0][1]+offset))
            #Test no intersection
            elif (to_test[0][1] < args[1]) or (to_test[0][0] > args[1] + args[2] - 1):
                remains.append(to_test[0])
            #Begins in range
            elif (args[1] <= to_test[0][0] <= args[1] + args[2]) and (to_test[0][1] > args[1] + args[2] - 1):
                next_test.append((to_test[0][0] + offset,args[1] + args[2] - 1 + offset))
                remains.append((args[1] + args[2],to_test[0][1]))
            #Ends in range
            elif (to_test[0][0] < args[1]) and (args[1] <= to_test[0][1] <= args[1] + args[2] - 1):
                next_test.append((args[1] + offset,to_test[0][1] + offset))
                remains.append((to_test[0][0],args[1]-1))
            
            to_test.popleft()
        
        to_test = deque(remains)
    
    next_test += remains
    to_test = deque(next_test)
    next_test = []

#Result part 2
print(min([s[0] for s in to_test]))
