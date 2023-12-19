input = open('aoc_10.txt', 'r')
lines = input.readlines()

pipe_map = list()

def find_next(positions):
    prev_pos = positions[0]
    curr_pos = positions[1]
    moving = (curr_pos[0] - prev_pos[0], curr_pos[1] - prev_pos[1])
    curr_pipe = pipe_map[curr_pos[0]][curr_pos[1]]
    next_pos = (0,0)
    
    if curr_pipe == '|':
        next_pos = (curr_pos[0] + moving[0], curr_pos[1])
    elif curr_pipe == '-':
        next_pos = (curr_pos[0], curr_pos[1] + moving[1])
    elif curr_pipe == 'L':
        if moving[0] > 0:
            next_pos = (curr_pos[0], curr_pos[1] + 1)
        else:
            next_pos = (curr_pos[0] - 1, curr_pos[1])
    elif curr_pipe =='J':
        if moving[0] > 0:
            next_pos = (curr_pos[0], curr_pos[1] - 1)
        else:
            next_pos = (curr_pos[0] - 1, curr_pos[1])
    elif curr_pipe == '7':
        if moving[0] < 0:
            next_pos = (curr_pos[0], curr_pos[1] - 1)
        else:
            next_pos = (curr_pos[0] + 1, curr_pos[1])
    elif curr_pipe == 'F':
        if moving[0] < 0:
            next_pos = (curr_pos[0], curr_pos[1] + 1)
        else:
            next_pos = (curr_pos[0] + 1, curr_pos[1])
    else:
        print('Something has gone bad wrong')
        quit()
    return(curr_pos, next_pos)
    

for line in lines:
    pipe_map.append(list(line.strip()))

start_position = (0,0)
for row in range(len(pipe_map)):
    for col in range(len(pipe_map[row])):
        if 'S' in pipe_map[row]:
            start_position = (row, pipe_map[row].index('S'))
            break

position_1 = (start_position, (start_position[0] - 1, start_position[1]))
position_2 = (start_position, (start_position[0] + 1, start_position[1]))

pipe_mask = [['.' for col in range(len(pipe_map[row]))] for row in range(len(pipe_map))]
pipe_mask[start_position[0]][start_position[1]] = '*'

while position_1[1] != position_2[1]:
    position_1 = find_next(position_1)
    pipe_mask[position_1[0][0]][position_1[0][1]] = '*'
    position_2 = find_next(position_2)
    pipe_mask[position_2[0][0]][position_2[0][1]] = '*'
pipe_mask[position_1[1][0]][position_1[1][1]] = '*'

viz_map = [['.' if pipe_mask[row][col] == '.' else pipe_map[row][col] for col in range(len(pipe_mask[row]))] for row in range(len(pipe_mask))]

def inside(row, col):
    edge_count = 0
    prev_corner = ''
    for x in range(col, len(viz_map[row])):
        pipe = viz_map[row][x]
        if pipe == '|' or pipe == 'S':
            edge_count += 1
        elif prev_corner + pipe == 'FJ' or prev_corner + pipe == 'L7':
            edge_count += 1
        if pipe in 'FJL7':
            prev_corner = pipe
    return edge_count % 2

count = 0
for row in range(len(viz_map)):
    for col in range(len(viz_map[row])):
        if '.' == viz_map[row][col]:
            count += inside(row, col)
print(count)