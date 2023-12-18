input = open('aoc_13.txt', 'r')
lines = [line.strip() for line in input.readlines()]

def difference(l: str, r: str) -> int:
    return sum(a != b for a,b in zip(l,r))

def find_symmetry(puzzle: list, smudges: bool) -> int:
    for i in range(1, len(puzzle)):
        if sum(difference(l,r) for l,r in zip(reversed(puzzle[:i]), puzzle[i:])) == 1:
            return i
    return 0

total = 0

i = 0
while i < len(lines):
    puzzle = []
    while i < len(lines) and len(lines[i]) > 0:
        puzzle.append(lines[i])
        i += 1
    
    rows_above_smudge = find_symmetry(puzzle, True)
    
    puzzle = list(zip(*puzzle))
    
    cols_left_smudge = find_symmetry(puzzle, True)
    
    if cols_left_smudge > 0 and rows_above_smudge > 0:
        print('Uh oh row {}'.format(i))
        quit()
    
    if cols_left_smudge > 0:
        total += cols_left_smudge
    if rows_above_smudge > 0:
        total += 100 * rows_above_smudge
    i += 1
    
print(total)
    
