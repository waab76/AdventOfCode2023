input = open('aoc_02.txt', 'r')
lines = input.readlines()

sum = 0

for line in lines:
    parts = line.strip().split(': ')
    game_number = int(parts[0][5:])
    rounds = parts[1].split('; ')
    max_red = 0
    max_blue = 0
    max_green = 0
    for round in rounds:
        colors = round.split(', ')
        for color in colors:
            color_parts = color.split(' ')
            if 'red' == color_parts[1] and int(color_parts[0]) > max_red:
                max_red = int(color_parts[0])
            elif 'blue' == color_parts[1]and int(color_parts[0]) > max_blue:
                max_blue = int(color_parts[0])
            elif 'green' == color_parts[1] and int(color_parts[0]) > max_green:
                max_green = int(color_parts[0])
    power = max_red * max_blue * max_green
    sum += power
print(sum)        
