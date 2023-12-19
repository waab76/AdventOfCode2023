input = open('aoc_19.txt', 'r')
blocks = input.read().split('\n\n')
rule_list = [line.strip() for line in blocks[0].split('\n')]

rules = {}
for rule in rule_list:
    label = rule.split('{')[0]
    routes = rule.split('{')[1][:-1].split(',')
    final = routes.pop(-1)
    my_routes = []
    for route in routes:
        my_routes.append({'condition': route.split(':')[0], 'rule': route.split(':')[1]})
    rules[label] = {'routes': my_routes, 'final': final}
    
total_combinations = 0
paths = [{'rule': 'in', 'gt': {'x': 0, 'm': 0, 'a': 0, 's': 0}, 'lt':{'x': 4001, 'm': 4001, 'a': 4001, 's': 4001}}]

while paths:
    path = dict(paths.pop())
    if 'R' == path['rule']:
        continue
    elif 'A' == path['rule']:
        score = 1
        for key in path['lt']:
            if path['lt'][key] - path['gt'][key] < 2:
                score *= 0
            score *= (path['lt'][key] - path['gt'][key] -1)
        total_combinations += score
        continue
    rule = rules[path['rule']]
    path['rule'] = rule['final']
    for route in rule['routes']:
        new_path = {}
        new_path['rule'] = route['rule']
        new_path['lt'], new_path['gt'] = {}, {}
        for key in path['lt']:
            new_path['lt'][key] = path['lt'][key]
            new_path['gt'][key] = path['gt'][key]
        key = route['condition'][0]
        val = int(route['condition'].split(':')[0][2:])
        if route['condition'][1] == '>':
            new_path['gt'][key] = max(new_path['gt'][key], val)
            path['lt'][key] = min(path['lt'][key], val + 1)
        elif route['condition'][1] == '<':
            new_path['lt'][key] = min(new_path['lt'][key], val)
            path['gt'][key] = max(path['gt'][key], val - 1)
        paths.append(new_path)
    paths.append(path)
print(total_combinations)
                
    

