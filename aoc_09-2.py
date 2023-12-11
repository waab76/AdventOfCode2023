input = open('aoc_09.txt', 'r')
lines = input.readlines()

sum_of_predictions = 0

for line in lines:
    base_nums = [int(i) for i in line.strip().split()]
    steps = [[0 for i in range(len(base_nums))] for j in range(len(base_nums))]
    steps[0] = base_nums
    for step in range(1, len(base_nums)):
        for num in range(0, len(base_nums) - step):
            steps[step][num] = steps[step - 1][num + 1] - steps[step - 1][num]
    prediction = 0
    for i in range(len(base_nums)-1, -1, -1):
        prediction = steps[i][0] - prediction
    sum_of_predictions += prediction
print(sum_of_predictions)
