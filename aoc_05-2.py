from collections import deque

input = open('aoc_05.txt', 'r')
lines = input.readlines()

range_data = [int(seed) for seed in lines[0].strip().split(':')[1].split()]
seed_ranges = deque()
for i in range(0, len(range_data), 2):
    seed_ranges.append((range_data[i], range_data[i+1]))

line = 1
while line < len(lines):
    if 'map' in lines[line]:
        mappings = []
        line += 1
        while line < len(lines) and len(lines[line].strip()) > 0:
            mappings.append([int(num) for num in lines[line].strip().split()])
            line += 1
            
        handled_ranges = deque()
        while len(seed_ranges) > 0:
            seed_range = seed_ranges.pop()
            for mapping in mappings:
                if seed_range[0] >= mapping[1] + mapping[2] or mapping[1] >= seed_range[0] + seed_range[1]:
                    next
                elif seed_range[0] < mapping[1]:
                    if seed_range[0] + seed_range[1] > mapping[1] + mapping[2]:
                        right_overrun = (mapping[1]+mapping[2], (seed_range[0]+seed_range[1]) - (mapping[1] + mapping[2]))
                        seed_range = (seed_range[0], mapping[1] + mapping[2] - seed_range[0])
                        seed_ranges.append(right_overrun)
                    left_overrun = (seed_range[0], mapping[1] - seed_range[0])
                    overlap = (mapping[0], seed_range[1] - left_overrun[1])
                    handled_ranges.append(overlap)
                    seed_range = left_overrun                    
                else:
                    right_overrun = (mapping[1]+mapping[2], (seed_range[0]+seed_range[1]) - (mapping[1] + mapping[2]))
                    overlap = (mapping[0], seed_range[1] - right_overrun[1])
                    handled_ranges.append(overlap)
                    if right_overrun[1] > 0:
                        seed_range = right_overrun
                    else:
                        seed_range = (0,0)
            if seed_range[1] > 0:
                handled_ranges.append(seed_range)
        seed_ranges = handled_ranges
    line += 1

range_starts = [item[0] for item in seed_ranges]
range_starts.sort()

# For some reason, I'm getting 9 spurious 0s in the final set of ranges
print(range_starts[9])