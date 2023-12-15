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
        if len(condition) < curr_group:
            return 0
        elif len(condition) == curr_group:
            return 0 if '.' in condition else count_arrangements('', new_groups)
        else:
            if '.' in condition[0:curr_group] or '#' == condition[curr_group]:
                return 0
            else:
                return count_arrangements(condition[curr_group + 1:], new_groups)
    else:
        return count_arrangements(condition[1:], groups) + count_arrangements('#' + condition[1:], groups)

possible_arrangements = 0

for line in lines:
    condition = ','.join([line.split()[0] for i in range(5)])
    groups = ','.join([line.strip().split()[1] for i in range(5)])
    possible_arrangements += count_arrangements(condition, groups)

print(possible_arrangements)
