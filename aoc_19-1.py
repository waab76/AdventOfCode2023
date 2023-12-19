input = open('aoc_19.txt', 'r')
blocks = input.read().split('\n\n')
rule_list = [line.strip() for line in blocks[0].split('\n')]
part_list = [line.strip() for line in blocks[1].split('\n')]

rules = {}
for rule in rule_list:
    label = rule.split('{')[0]
    routes = rule.split('{')[1][:-1].split(',')
    final = routes.pop(-1)
    my_routes = []
    for route in routes:
        my_routes.append({'condition': route.split(':')[0], 'rule': route.split(':')[1]})
    rules[label] = {'routes': my_routes, 'final': final}
    
parts = []
total_score = 0
for part in part_list:
    x, m, a, s = 0, 0, 0, 0
    for val in part[1:-1].split(','):
        if 'x' == val.split('=')[0]:
            x = int(val.split('=')[1])
        elif 'm' == val.split('=')[0]:
            m = int(val.split('=')[1])
        elif 'a' == val.split('=')[0]:
            a = int(val.split('=')[1])
        elif 's' == val.split('=')[0]:
            s = int(val.split('=')[1])
        else:
            print('wtf')
    rule = 'in'
    while rule not in ['R', 'A']:
        matched = False
        for route in rules[rule]['routes']:
            if eval(route['condition']):
                matched = True
                rule = route['rule']
                break
        if not matched:
            rule = rules[rule]['final']
    if rule == 'A':
        total_score += x
        total_score += m
        total_score += a
        total_score += s
print(total_score)
                
    
