input = open('aoc_13.txt', 'r')
lines = input.readlines()

def find_symmetry(puzzle) -> int:
    mismatches = [0 for i in range(len(puzzle) - 1)]
    
    for row in range(len(puzzle) - 1):
        delta = 0
        while row - delta >= 0 and row + 1 + delta < len(puzzle):
            mismatches[row] += sum([0 if puzzle[row - delta][i] == puzzle[row+1+delta][i] else 1 for i in range(len(puzzle[row]))])
            delta += 1
    smudge_rows = 0
    try:
        smudge_rows = mismatches.index(1) + 1
        print(mismatches)
        print(smudge_rows)
    except:
        pass
    return smudge_rows

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
# 35849 is to low
print(total)
    
