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
print('Starting nodes {}'.format(current_nodes))
step = 0
while len(current_nodes) > 0:
    # print('{} nodes going {}'.format(len(current_nodes), directions[step]))
    next_nodes = []
    for node in current_nodes:
        next_nodes.append(nodes[node][directions[step]])
    z_count = 0
    for node in next_nodes:
        if 'Z' in node[2]:
            z_count += 1
    if z_count < len(current_nodes):
        current_nodes = next_nodes
        step = (step + 1) % len(directions)
    else:
        current_nodes = []

# 107450 is too low
print(step)
    
