input = open('aoc_03.txt', 'r')
lines = input.readlines()

value_sum = 0

schematic = []

def is_part_number(check_row, check_start_col, check_end_col):
    for i in range(max([0,check_row - 1]), min([check_row + 2, len(schematic)])):
        for j in range(max([0,check_start_col - 1]), min([check_end_col + 2, len(schematic[check_row])])):
            try:
                if schematic[i][j] not in '0123456789.':
                    # print('{} on row {} has adjacent symbol {} at location [{},{}]'.format(schematic[check_row][check_start_col:check_end_col+1], check_row, schematic[i][j], i, j))
                    return True
            except:
                print('Error checking location [{},{}]'.format(i,j))
    return False

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
            if is_part_number(row, start_col, end_col):
                value_sum += int(schematic[row][start_col:end_col+1])
        col += 1
        
print(value_sum)
