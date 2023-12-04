f = open("2023/Advent2023-4.txt","r").read().split('\n')

result_1 = 0
wins = []
for line in f:
    card = [s.strip() for s in line.split(':')[1].strip().split('|')]

    winning_num = card[0].split()
    my_num = card[1].split()

    total_win = sum([1 for n in my_num if n in winning_num])
    wins.append(total_win)
    
    #Part 1 result
    if total_win > 0:
        result_1 += 2**(total_win-1)

print(result_1)

#Part 2 result
cards = [1 for i in range(len(wins))]

for i,w in enumerate(wins):
    for t in range(i+1,min(i+1+w,len(cards))):
        cards[t] += cards[i]
    
print(sum(cards))
