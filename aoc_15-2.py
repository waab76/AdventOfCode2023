input = open('aoc_15.txt', 'r')
lines = input.readlines()

def holiday_ascii_string_helper(sequence: str) -> int:
    value = 0
    for char in sequence:
        value += ord(char)
        value *= 17
        value %= 256
    return value

lens_boxes = [list() for i in range(256)]
init_seqs = lines[0].strip().split(',')

for sequence in init_seqs:
    label = sequence.strip().split('=')[0] if '=' in sequence else sequence.strip().split('-')[0]
    focal_length = int(sequence.strip().split('=')[1]) if '=' in sequence else 0
    target_box = holiday_ascii_string_helper(label)
    
    if '-' in sequence:
        for i in range(len(lens_boxes[target_box])):
            if lens_boxes[target_box][i]['label'] == label:
                lens_boxes[target_box].pop(i)
                break
    else:
        found = False
        for i in range(len(lens_boxes[target_box])):
            if lens_boxes[target_box][i]['label'] == label:
                lens_boxes[target_box][i]['focal_length'] = focal_length
                found = True
                break
        if not found:
            lens_boxes[target_box].append({'label': label, 'focal_length': focal_length})

focusing_power = 0
for i in range(256):
    box_val = i + 1
    for j in range(len(lens_boxes[i])):
        slot_number = j + 1
        focusing_power += box_val * slot_number * lens_boxes[i][j]['focal_length']

print(focusing_power)