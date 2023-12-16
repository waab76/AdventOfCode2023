input = open('aoc_16.txt', 'r')
lines = [line.strip() for line in input.readlines()]

def count_energized(start_point: map) -> int:
    energized = set()
    processed = list()

    beams_to_handle = list()
    beams_to_handle.append(start_point)

    while len(beams_to_handle) > 0:
        curr_beam = beams_to_handle.pop()
        if curr_beam in processed:
            continue
        energized.add((curr_beam['row'], curr_beam['col']))
        curr_tile = lines[curr_beam['row']][curr_beam['col']]
        
        if curr_beam['direction'] == 'R':
            if curr_tile in '.-' and curr_beam['col'] + 1 < len(lines[0]):
                beams_to_handle.append({'row': curr_beam['row'], 'col': curr_beam['col'] + 1, 'direction': 'R'})
            elif curr_tile == '/' and curr_beam['row'] - 1 >= 0:
                beams_to_handle.append({'row': curr_beam['row'] - 1, 'col': curr_beam['col'], 'direction': 'U'})
            elif curr_tile == '\\' and curr_beam['row'] + 1 < len(lines):
                beams_to_handle.append({'row': curr_beam['row'] + 1, 'col': curr_beam['col'], 'direction': 'D'})
            elif curr_tile == '|':
                if curr_beam['row'] - 1 >= 0:
                    beams_to_handle.append({'row': curr_beam['row'] - 1, 'col': curr_beam['col'], 'direction': 'U'})
                if curr_beam['row'] + 1 < len(lines):
                    beams_to_handle.append({'row': curr_beam['row'] + 1, 'col': curr_beam['col'], 'direction': 'D'})
        elif curr_beam['direction'] == 'L':
            if curr_tile in '.-' and curr_beam['col'] - 1 >= 0:
                beams_to_handle.append({'row': curr_beam['row'], 'col': curr_beam['col'] - 1, 'direction': 'L'})
            elif curr_tile == '\\' and curr_beam['row'] - 1 >= 0:
                beams_to_handle.append({'row': curr_beam['row'] - 1, 'col': curr_beam['col'], 'direction': 'U'})
            elif curr_tile == '/' and curr_beam['row'] + 1 < len(lines):
                beams_to_handle.append({'row': curr_beam['row'] + 1, 'col': curr_beam['col'], 'direction': 'D'})
            elif curr_tile == '|':
                if curr_beam['row'] - 1 >= 0:
                    beams_to_handle.append({'row': curr_beam['row'] - 1, 'col': curr_beam['col'], 'direction': 'U'})
                if curr_beam['row'] + 1 < len(lines):
                    beams_to_handle.append({'row': curr_beam['row'] + 1, 'col': curr_beam['col'], 'direction': 'D'})
        elif curr_beam['direction'] == 'U':
            if curr_tile in '.|' and curr_beam['row'] - 1 >= 0:
                beams_to_handle.append({'row': curr_beam['row'] - 1, 'col': curr_beam['col'], 'direction': 'U'})
            elif curr_tile == '/' and curr_beam['col'] + 1 < len(lines[0]):
                beams_to_handle.append({'row': curr_beam['row'], 'col': curr_beam['col'] + 1, 'direction': 'R'})
            elif curr_tile == '\\' and curr_beam['col'] - 1 >= 0:
                beams_to_handle.append({'row': curr_beam['row'], 'col': curr_beam['col'] - 1, 'direction': 'L'})
            elif curr_tile == '-':
                if curr_beam['col'] - 1 >= 0:
                    beams_to_handle.append({'row': curr_beam['row'], 'col': curr_beam['col'] - 1, 'direction': 'L'})
                if curr_beam['col'] + 1 < len(lines[0]):
                    beams_to_handle.append({'row': curr_beam['row'], 'col': curr_beam['col'] + 1, 'direction': 'R'})
        elif curr_beam['direction'] == 'D':
            if curr_tile in '.|' and curr_beam['row'] + 1 < len(lines):
                beams_to_handle.append({'row': curr_beam['row'] + 1, 'col': curr_beam['col'], 'direction': 'D'})
            elif curr_tile == '\\' and curr_beam['col'] + 1 < len(lines[0]):
                beams_to_handle.append({'row': curr_beam['row'], 'col': curr_beam['col'] + 1, 'direction': 'R'})
            elif curr_tile == '/' and curr_beam['col'] - 1 >= 0:
                beams_to_handle.append({'row': curr_beam['row'], 'col': curr_beam['col'] - 1, 'direction': 'L'})
            elif curr_tile == '-':
                if curr_beam['col'] - 1 >= 0:
                    beams_to_handle.append({'row': curr_beam['row'], 'col': curr_beam['col'] - 1, 'direction': 'L'})
                if curr_beam['col'] + 1 < len(lines[0]):
                    beams_to_handle.append({'row': curr_beam['row'], 'col': curr_beam['col'] + 1, 'direction': 'R'})
        processed.append(curr_beam)

    return(len(energized))

print(count_energized({'row':0, 'col':0, 'direction':'R'}))