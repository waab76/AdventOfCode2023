input = open('aoc_06.txt', 'r')
lines = input.readlines()

time = int(lines[0].split(':')[1].strip().replace(' ', ''))
record = int(lines[1].split(':')[1].strip().replace(' ', ''))
ways = 0

for hold in range(time):
    distance = hold * (time - hold)
    if distance > record:
        ways += 1

print(ways)
