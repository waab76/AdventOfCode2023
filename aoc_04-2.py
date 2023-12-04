input = open('aoc_04.txt', 'r')
lines = input.readlines()

copies = [1 for i in range(218)]

card = 0
for line in lines:
    line_parts = line.strip().split(':')
    card_parts = line_parts[1].split('|')
    winners = set([int(i) for i in card_parts[0].split()])
    guesses = set([int(i) for i in card_parts[1].split()])
    match_count = len(guesses.intersection(winners))
    
    for win in range(1, match_count+1):
        if (card + win) < 218:
            copies[card + win] += copies[card]
    card += 1

print(sum(copies))