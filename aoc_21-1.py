input = open('aoc_21.txt', 'r')
garden = [list(line.strip()) for line in input.read().split('\n')]

# Find the start
start = (-1,-1)
for row in range(len(garden)):
    if 'S' in garden[row]:
        start = (row, garden[row].index('S'))

positions = list()
positions.append((start[0], start[1], 0))
visited = set()
endpoints = set()

while positions:
    curr_pos = positions.pop(0)
    if curr_pos in visited:
        continue
    else:
        visited.add(curr_pos)
    if curr_pos[2] == 64:
        endpoints.add((curr_pos[0], curr_pos[1]))
        continue
    
    if curr_pos[0] - 1 > 0 and garden[curr_pos[0] - 1][curr_pos[1]] != '#':
        positions.append((curr_pos[0] - 1, curr_pos[1], curr_pos[2] + 1))
    if curr_pos[0] + 1 < len(garden) and garden[curr_pos[0] + 1][curr_pos[1]] != '#':
        positions.append((curr_pos[0] + 1, curr_pos[1], curr_pos[2] + 1))
    if curr_pos[1] - 1 > 0 and garden[curr_pos[0]][curr_pos[1] - 1] != '#':
        positions.append((curr_pos[0], curr_pos[1] - 1, curr_pos[2] + 1))
    if curr_pos[1] + 1 < len(garden[curr_pos[0]]) and garden[curr_pos[0]][curr_pos[1] + 1] != '#':
        positions.append((curr_pos[0], curr_pos[1] + 1, curr_pos[2] + 1))
    
print(len(endpoints))