input = open('aoc_04.txt', 'r')
lines = input.readlines()

total_points = 0

for line in lines:
    line_parts = line.strip().split(':')
    card_parts = line_parts[1].split('|')
    winners = set([int(i) for i in card_parts[0].split()])
    guesses = set([int(i) for i in card_parts[1].split()])
    
    matches = guesses.intersection(winners)
    
    points = 0
    if len(matches) > 0:
        points = 2 ** (len(matches) - 1)
    total_points += points

print(total_points)