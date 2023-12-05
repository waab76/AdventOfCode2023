input = open('aoc_05.txt', 'r')
lines = input.readlines()

seeds = [int(seed) for seed in lines[0].strip().split(':')[1].split()]

line = 1
while line < len(lines):
    if 'map' in lines[line]:
        mappings = []
        line += 1
        while line < len(lines) and len(lines[line].strip()) > 0:
            mappings.append([int(num) for num in lines[line].strip().split()])
            line += 1
        for seed_num in range(len(seeds)):
            seed = seeds[seed_num]
            for mapping in mappings:
                if seed >= mapping[1] and seed < mapping[1] + mapping[2]:
                    seed = seed - mapping[1] + mapping[0]
                    break
            seeds[seed_num] = seed
    line += 1
print(min(seeds))