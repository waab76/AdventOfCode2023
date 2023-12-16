from functools import cache

input = open('aoc_14.txt', 'r')
lines = input.readlines()

def rotate_left(matrix) -> list:
    return [''.join([matrix[col][row] for col in range(len(matrix))]) for row in range(len(matrix[0])-1, -1, -1)]

def rotate_right(matrix) -> list:
    return [''.join([matrix[col][row] for col in range(len(matrix)-1, -1, -1)]) for row in range(len(matrix[0]))]

def roll_left(row_string) -> list:
    matrix_row = list(row_string)
    for col in range(len(matrix_row)):
        if 'O' == matrix_row[col]:
            i = col
            while i > 0 and matrix_row[i - 1] not in 'O#':
                i -= 1
            if i >= 0 and matrix_row[i] not in 'O#':
                matrix_row[i] = matrix_row[col]
                matrix_row[col] = '.'
    return ''.join(matrix_row)

platform = []
state_cache = []

for line in lines:
    platform.append(line.strip())

current_state = platform

while current_state not in state_cache:
    state_cache.append(current_state)
    
    platform = rotate_left(platform)
    for cycle_step in range(4):
        for row in range(len(platform)):
            platform[row] = roll_left(platform[row])
        platform = rotate_right(platform)
    platform = rotate_right(platform)
    current_state = platform
    
cycle_start = state_cache.index(current_state)
cycle_period = len(state_cache) - cycle_start

print('Cycle starts at {}'.format(cycle_start))
print('Cycle repeats at {} and {}'.format(cycle_start + cycle_period, cycle_start + cycle_period + cycle_period))

desired_cycles = 1000000000
required_cycles = cycle_start  + (desired_cycles - cycle_start) % cycle_period

platform = state_cache[required_cycles]

load = 0
for row in range(len(platform)):
    for col in range(len(platform[row])):
        if 'O' == platform[row][col]:
            load += len(platform) - row

print(load)
