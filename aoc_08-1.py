input = open('aoc_08.txt', 'r')
lines = input.readlines()

directions = lines[0].strip()
nodes = {}

for i in range(2, len(lines)):
    node_id = lines[i][0:3]
    nodes[node_id] = {'L': lines[i][7:10], 'R': lines[i][12:15]}
    # print('{} -> {}'.format(node_id, nodes[node_id]))
    # quit()

current_node = 'AAA'
steps = 0
while 'ZZZ' not in current_node:
    # print('On node {} with children {}'.format(current_node, nodes[current_node]))
    current_node = nodes[current_node][directions[steps % len(directions)]]
    # print('Moving {} to {}'.format(directions[steps % len(directions)], current_node))
    steps += 1
    
print(steps)
    