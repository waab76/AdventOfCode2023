input = open('aoc_14.txt', 'r')
lines = input.readlines()

platform = []

for line in lines:
    platform.append(list(line.strip()))
    
# Roll North
for row in range(len(platform)):
    for col in range(len(platform[row])):
        if 'O' == platform[row][col]:
            i = row
            while i > 0 and platform[i-1][col] not in 'O#':
                i -= 1
            if i >= 0 and platform[i][col] not in 'O#':
                platform[i][col] = 'O'
                platform[row][col] = '.'
load = 0
for row in range(len(platform)):
    for col in range(len(platform[row])):
        if 'O' == platform[row][col]:
            load += len(platform) - row
print(load)