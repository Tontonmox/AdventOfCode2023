def calc_strength(card_count):
    hand_strength = 1
    #5 of a kind
    if len(card_count) == 1:
        hand_strength = 7
    #4 of a kind
    elif max(card_count) == 4:
        hand_strength = 6
    #Full house
    elif len(card_count) == 2 and max(card_count) == 3:
        hand_strength = 5
    #Three of a kind
    elif len(card_count) == 3 and max(card_count) == 3:
        hand_strength = 4
    #Two pairs
    elif card_count.count(2) == 2:
        hand_strength = 3
    #One pair
    elif len(card_count) == 4:
        hand_strength = 2
    
    return hand_strength


f = open("2023/Advent2023-7.txt","r").read().split('\n')

#Part 1
game = []
for l in f:
    hand,bet = l.split()
    handv = [int(h.replace('T','10').replace('J','11').replace('Q','12').replace('K','13').replace('A','14')) for h in hand]
    card_count = ([handv.count(a) for a in set(handv)])

    hand_strength = calc_strength(card_count)
    
    game.append((hand_strength,handv,bet))

game.sort()
result_1 = 0
for i,g in enumerate(game):
    result_1 += int(g[2]) * (i + 1)

print(result_1)

#Part 2
game = []
for l in f:
    hand,bet = l.split()
    handv = [int(h.replace('T','10').replace('J','1').replace('Q','12').replace('K','13').replace('A','14')) for h in hand]
    #Card count sans les jokers
    card_count = sorted([handv.count(a) for a in set(handv) if a > 1])
    joker_count = handv.count(1)
    if len(card_count) > 0:
        card_count[-1] += joker_count
    else:
        card_count.append(joker_count)

    hand_strength = calc_strength(card_count)

    game.append((hand_strength,handv,bet))

game.sort()
result_2 = 0
for i,g in enumerate(game):
    result_2 += int(g[2]) * (i + 1)

print(result_2)

