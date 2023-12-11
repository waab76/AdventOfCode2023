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
    pipe_map.append(line.strip())

start_position = (0,0)
for row in range(len(pipe_map)):
    if 'S' in pipe_map[row]:
        start_position = (row, pipe_map[row].find('S'))
        break

position_1 = (start_position, (start_position[0] - 1, start_position[1]))
position_2 = (start_position, (start_position[0] + 1, start_position[1]))
distance = 1

while position_1[1] != position_2[1]:
    position_1 = find_next(position_1)
    position_2 = find_next(position_2)
    distance += 1

print(distance)