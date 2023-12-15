input = open('aoc_15.txt', 'r')
lines = input.readlines()

def holiday_ascii_string_helper(sequence: str) -> int:
    value = 0
    for char in sequence:
        value += ord(char)
        value *= 17
        value %= 256
    return value

init_seqs = lines[0].strip().split(',')

hash_sum = 0
for sequence in init_seqs:
    hash_sum += holiday_ascii_string_helper(sequence)

print(hash_sum)