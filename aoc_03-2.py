input = open('aoc_03.txt', 'r')
lines = input.readlines()

value_sum = 0

schematic = []
gear_part_adjacency = {}

def check_gear_adjacency(check_row, check_start_col, check_end_col):
    for i in range(max([0,check_row - 1]), min([check_row + 2, len(schematic)])):
        for j in range(max([0,check_start_col - 1]), min([check_end_col + 2, len(schematic[check_row])])):
            if '*' == schematic[i][j]:
                # print('{} on row {} is adjacent to gear at location [{},{}]'.format(schematic[check_row][check_start_col:check_end_col+1], check_row, i, j))
                if (i,j) not in gear_part_adjacency:
                    gear_part_adjacency[(i,j)] = []
                gear_part_adjacency[(i,j)].append(int(schematic[check_row][check_start_col:check_end_col+1]))

for line in lines:
    schematic.append(line.strip())
    
for row in range(len(schematic)):
    col = 0
    while col < len(schematic[row]):
        if schematic[row][col] in '0123456789':
            start_col = col
            while col + 1 < len(schematic[row]) and schematic[row][col+1] in '0123456789':
                col += 1
            end_col = col
            check_gear_adjacency(row, start_col, end_col)
        col += 1

for gear in gear_part_adjacency:
    # print('Gear at {} has {} part(s)'.format(gear, len(gear_part_adjacency[gear])))
    if len(gear_part_adjacency[gear]) == 2:
        value_sum += gear_part_adjacency[gear][0] * gear_part_adjacency[gear][1]
        
print(value_sum)

