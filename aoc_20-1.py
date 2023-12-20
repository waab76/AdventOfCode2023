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

flip_flops = {}
conjunctions = {}
for gate in gates:
    if gates[gate]['type'] == '&':
        conjunctions[gate] = {}
    elif gates[gate]['type'] == '%':
        flip_flops[gate] = 0
for gate in gates:
    for out in gates[gate]['outputs']:
        if out in conjunctions:
            conjunctions[out][gate] = 0

pulses_sent = []
low_pulses = 0
high_pulses = 0
for input_pulse in range(1000):
    pulses_sent.append((0, 'broadcaster', 'button')) # Send a low pulse to broadcast
    while pulses_sent:
        pulse = pulses_sent.pop(0)
        if pulse[0]:
            high_pulses += 1
        else:
            low_pulses += 1
        if pulse[1] not in gates:
            continue
        if gates[pulse[1]]['type'] == 'broadcaster':
            for output in gates[pulse[1]]['outputs']:
                pulses_sent.append((pulse[0], output, 'broadcaster'))
        elif gates[pulse[1]]['type'] == '&': # Conjunction
            conjunctions[pulse[1]][pulse[2]] = pulse[0] # First remember the incoming pulse
            all_high = True
            for incoming in conjunctions[pulse[1]]:
                if conjunctions[pulse[1]][incoming]:
                    pass
                else:
                    all_high = False
                    break
            for output in gates[pulse[1]]['outputs']:
                pulses_sent.append((0 if all_high else 1, output, pulse[1]))
        elif gates[pulse[1]]['type'] == '%': # Flip-flop
            if pulse[0]: # Ignore high pulses
                continue
            flip_flops[pulse[1]] = (flip_flops[pulse[1]] + 1 ) % 2 # Change state
            for output in gates[pulse[1]]['outputs']:
                pulses_sent.append((flip_flops[pulse[1]], output, pulse[1])) # Send high if on, low if off

print(low_pulses * high_pulses)