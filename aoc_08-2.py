from math import gcd, lcm

input = open('aoc_08.txt', 'r')
lines = input.readlines()

directions = lines[0].strip()
nodes = {}

for i in range(2, len(lines)):
    node_id = lines[i][0:3]
    nodes[node_id] = {'L': lines[i][7:10], 'R': lines[i][12:15]}

current_nodes = []

for node in nodes:
    if 'A' == node[2]:
        current_nodes.append(node)
print(current_nodes)
step = 0
steps_to_z = [0 for i in range(len(current_nodes))]
while len(current_nodes) > 0 and sum([1 if found > 0 else 0 for found in steps_to_z]) < len(steps_to_z):
    next_nodes = []
    for i in range(len(current_nodes)):
        next_node = nodes[current_nodes[i]][directions[step%len(directions)]]
        if next_node[2] == 'Z':
            steps_to_z[i] = step + 1
            print(steps_to_z)
        next_nodes.append(next_node)
    # print('Step {}: {} moving {} to {}'.format(step, current_nodes, directions[step%len(directions)], next_nodes))
    current_nodes = next_nodes
    step += 1


# 107450 is too low
# 10921547990923 if I do step + 1  <-- This one is right
# 107686606850205451200 is too high
# 1417279311207866321565525 if I do step - 1
curr_lcm = 1
for i in range(len(steps_to_z)):
    curr_lcm = lcm(curr_lcm, steps_to_z[i])
print(curr_lcm)
    
