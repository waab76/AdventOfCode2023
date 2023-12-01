input = open('aoc_01.txt', 'r')
lines = input.readlines()

def is_digit(check):
    return check in '0123456789'

value_sum = 0

for line in lines:
    first_digit = ''
    last_digit = ''
    for i in range(len(line)):
        if is_digit(line[i]):
            if '' == first_digit:
                first_digit = line[i]
            last_digit = line[i]
    line_value = '{}{}'.format(first_digit, last_digit)
    value_sum += int(line_value)

print(value_sum)