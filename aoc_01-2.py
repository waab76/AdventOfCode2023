input = open('aoc_01.txt', 'r')
lines = input.readlines()

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digit_values = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
                'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


value_sum = 0

for line in lines:
    first_digit = ''
    first_digit_position = len(line) + 1
    last_digit = ''
    last_digit_position = 0
    
    for digit in digits:
        digit_position = line.find(digit)
        if digit_position >= 0:
            # print('Found {} at position {}'.format(digit_values[digit], digit_position))
            if digit_position < first_digit_position:
                first_digit = digit_values[digit]
                first_digit_position = digit_position
            if digit_position > last_digit_position:
                last_digit = digit_values[digit]
                last_digit_position = digit_position
        digit_position = line.rfind(digit)
        if digit_position >= 0:
            # print('Found {} at position {}'.format(digit_values[digit], digit_position))
            if digit_position < first_digit_position:
                first_digit = digit_values[digit]
                first_digit_position = digit_position
            if digit_position > last_digit_position:
                last_digit = digit_values[digit]
                last_digit_position = digit_position
    line_value = '{}{}'.format(first_digit, last_digit)
    # print(line_value)
    value_sum += int(line_value)

print(value_sum)
