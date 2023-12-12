input = open('aoc_11.txt', 'r')
lines = input.readlines()

total_steps = 0 

pre_map = [line.strip() for line in lines]
empty_rows = set()
empty_cols = set()
galaxies = list()
for col in range(len(pre_map[0])):
    galaxies_found = 0
    for row in range(len(pre_map)):
        if '#' not in pre_map[row]:
            empty_rows.add(row)
        if '#' == pre_map[row][col]:
            galaxies_found += 1
            galaxies.append((row, col))
    if 0 == galaxies_found:
        empty_cols.add(col)

pairs = 0
for one in range(len(galaxies) - 1):
    for two in range(one + 1, len(galaxies)):
        pairs += 1
        row_dist = abs(galaxies[two][0] - galaxies[one][0])
        col_dist = abs(galaxies[two][1] - galaxies[one][1])
        steps = row_dist + col_dist
        for row in empty_rows:
            if min(galaxies[one][0], galaxies[two][0]) < row and max(galaxies[one][0], galaxies[two][0]) > row:
                steps += 999999
        for col in empty_cols:
            if min(galaxies[one][1], galaxies[two][1]) < col and max(galaxies[one][1], galaxies[two][1]) > col:
                steps += 999999
        total_steps += steps
print(total_steps)
