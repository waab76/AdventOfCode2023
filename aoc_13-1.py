input = open('aoc_13.txt', 'r')
lines = input.readlines()

def find_symmetry(puzzle) -> int:
    match = False
    for row in range(len(puzzle) - 1):
        if puzzle[row] == puzzle[row+1]:
            # print('Match:\n{} : {}\n{} : {}'.format(row, puzzle[row], row + 1, puzzle[row+1]))
            match = True
            delta = 1
            while row - delta >= 0 and row + 1 + delta < len(puzzle):
                if puzzle[row - delta] != puzzle[row + 1 + delta]:
                    # print('Broken:\n{} : {}\n{} : {}'.format(row - delta, puzzle[row - delta], row + 1 + delta, puzzle[row+1+delta]))
                    match = False
                    break
                else:
                    delta += 1
            if match:
                # print('Symmetry at rows {} and {}'.format(row, row+1))
                return row + 1
    return 0

total = 0

i = 0
while i < len(lines):
    puzzle = []
    puzzle_val = 0
    while i < len(lines) and len(lines[i].strip()) > 0:
        puzzle.append(lines[i].strip())
        i += 1
    
    puzzle_val = 100 * find_symmetry(puzzle)
    
    if puzzle_val == 0:
        # print('No symmetry found, rotating')
        new_puz = [[puzzle[col][row] for col in range(len(puzzle)-1, -1, -1)] for row in range(len(puzzle[0]))]
        puzzle_val = find_symmetry(new_puz)
    
    total += puzzle_val
    i += 1

# 25369 is to low
print(total)
    