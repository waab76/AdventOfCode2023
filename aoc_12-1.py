from functools import cache
input = open('aoc_12.txt', 'r')
lines = input.readlines()

@cache
def count_arrangements(condition, groups) -> int:
    if len(groups) == 0:
        return 1 if '#' not in condition else 0
    elif len(condition) == 0:
        return 0
    
    num_groups = [int(num) for num in groups.split(',')]
    curr_group = num_groups[0]
    new_groups = ','.join([str(num) for num in num_groups[1:]]) if len(num_groups) > 1 else ''
    
    if '.' == condition[0]:
        return count_arrangements(condition[1:], groups)
    elif '#' == condition[0]:
        # Must try to consume the first group or return 0
        if len(condition) >= curr_group and sum([1 if condition[i] in '?#' else 0 for i in range(curr_group)]) == curr_group:
            if len(new_groups) > 0 and len(condition) > curr_group and condition[curr_group] == '#':
                return 0
            return count_arrangements(condition[curr_group:], new_groups)
        else:
            return count_arrangements(condition[1:], groups)
    else:
        return count_arrangements(condition[1:], groups) + count_arrangements('#' + condition[1:], groups)

possible_arrangements = 0

for line in lines:
    condition = line.split()[0]
    groups = line.strip().split()[1]
    possible_arrangements += count_arrangements(condition, groups)

# 33803 is too high, I'm over counting, 27480 is wrong
print(possible_arrangements)