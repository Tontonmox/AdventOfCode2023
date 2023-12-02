f = open("2023/Advent2023-2.txt","r").read().split('\n')

max_cubes = {'red' : 12,
       'green' : 13,
       'blue' : 14
       }

game_count = 1
result_1 = 0
result_2 = 0

for line in f:
    line = line.replace(', ',',')
    sets = [g.strip().split(',') for g in line.split(':')[1].strip().split(';')]

    tests = [test.split() for set in sets for test in set]
    
    #Part 1 :
    nb_errors = sum([1 for test in tests if int(test[0]) > max_cubes[test[1]]])

    if nb_errors == 0:
        result_1 += game_count

    #Part 2 :
    blue_cubes = max([int(test[0]) for test in tests if test[1] == 'blue'])
    red_cubes = max([int(test[0]) for test in tests if test[1] == 'red'])
    green_cubes = max([int(test[0]) for test in tests if test[1] == 'green'])
    result_2 += blue_cubes * red_cubes * green_cubes
    
    game_count += 1

print(result_1)
print(result_2)
