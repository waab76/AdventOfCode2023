input = open('aoc_20.txt', 'r')
data = input.read().split('\n')

gates = {}

for line in data:
    parts = line.split(' -> ')
    gate_type = 'broadcaster'
    label = 'broadcaster'
    if parts[0][0] in '%&':
        gate_type = parts[0][0]
        label = parts[0][1:].strip()
    outputs = [output.strip() for output in parts[1].split(',')]
    gates[label] = {'type': gate_type, 'outputs': outputs}

pulses_sent = []
flip_flops = {}

low_pulses = 0
high_pulses = 0
for input_pulse in range(1000):
    pulses_sent.append((0, 'broadcaster')) # Send a low pulse to broadcast
    while pulses_sent:
        pulse = pulses_sent.pop(0)
        if pulse[0]:
            high_pulses += 1
        else:
            low_pulses += 1
        if gates[pulse[1]]['type'] == 'broadcaster':
            print('broadcaster')
            for output in gates[pulse[1]]['outputs']:
                pulses_sent.append((pulse[0], output))
        elif gates[pulse[1]]['type'] == '&':
            print('conjunction')
        elif gates[pulse[1]]['type'] == '%':
            print('flip-flop')

print(low_pulses * high_pulses)