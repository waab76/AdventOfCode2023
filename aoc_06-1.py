input = open('aoc_06.txt', 'r')
lines = input.readlines()

times = [int(datum) for datum in lines[0].split(':')[1].strip().split()]
records = [int(datum) for datum in lines[1].split(':')[1].strip().split()]
ways = [0 for i in range(len(times))]

for race in range(len(times)):
    for hold in range(times[race]):
        distance = hold * (times[race] - hold)
        if distance > records[race]:
            ways[race] += 1

result = 1
for way in ways:
    result *= way

print(result)