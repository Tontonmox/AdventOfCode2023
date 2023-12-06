f = open("2023/Advent2023-6.txt","r").read().split('\n')

#Part 1
times = [int(l.strip()) for l in f[0].split(':')[1].split()]
dists = [int(l.strip()) for l in f[1].split(':')[1].split()]

result_1 = 1

for i,t in enumerate(times):
    wins = sum([1 for n in range(t) if n * (t-n) > dists[i]])
    result_1 *= wins

print(result_1)

#Part 2
time_2 = int(f[0].replace(' ','').split(':')[1])
dist_2 = int(f[1].replace(' ','').split(':')[1])

for x in range(time_2):
    if x * (time_2 - x) > dist_2:
        break

for y in range(time_2,0,-1):
    if y* (time_2 - y) > dist_2:
        break

print(y - x + 1)
