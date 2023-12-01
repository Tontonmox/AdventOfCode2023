import string
import re

f = open("2023/Advent2023-1.txt","r").read().split('\n')

digits = [('one','1'),
          ('two','2'),
          ('three','3'),
          ('four','4'),
          ('five','5'),
          ('six','6'),
          ('seven','7'),
          ('eight','8'),
          ('nine','9')]

res_part1 = 0
res_part2 = 0

for line in f:
    # Part 1 : Filter all letter from the string then make a number from first digit / last digit and add it to the result
    filtered = ''.join(c for c in line if c not in string.ascii_letters)
    res_part1 += int(filtered[0] + filtered[-1])

    # Part 2
    # Find the position of all written digits in the line
    pos = []
    for d in digits:
        pos += [(m.start(),d[1]) for m in re.finditer(d[0], line)]
    pos.sort()

    #Add the digits you found in the string, where the string starts
    for i,p in enumerate(pos) :
        line = line[:p[0]+i] + p[1] + line[p[0]+i:]

    #Apply part 1 formula
    filtered = ''.join(c for c in line if c not in string.ascii_letters)
    res_part2 += int(filtered[0] + filtered[-1])

print(res_part1)
print(res_part2)
