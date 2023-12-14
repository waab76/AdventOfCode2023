input = open('aoc_13.txt', 'r')
lines = input.readlines()

def find_symmetry(puzzle) -> int:
    for i in range(len(puzzle) - 1):
        if puzzle[i] == puzzle[i+1]:
            for j in range(1, min(i, len(puzzle) - (i+1))):
                if puzzle[i - j] != puzzle[i + 1 + j]:
                    break
            return i
    return 0

total = 0

i = 0
while i < len(lines):
    puzzle = []
    puzzle_val = 0
    while len(lines[i].strip()) > 0:
        puzzle.append(lines[i].strip())
        i += 1
    
    puzzle_val = 100 * find_symmetry(puzzle)
    
    if puzzle_val == 0:
        # transpose 90 degrees clockwise
        new_puz = [[puzzle[col][row] for col in range(len(puzzle)-1, -1, -1)] for row in range(len(puzzle[0]))]
        puzzle_val = find_symmetry(new_puz)
    
    total += puzzle_val
    i += 1
    
print(total)
    