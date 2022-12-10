from sys import stdin

val = 1
cycle = 0
values = []

for line in stdin.read().strip().split('\n'):
    vals = line.split()
    for i in range(len(vals)):
        values.append(abs(len(values) % 40 - val) < 2)
    if len(vals) > 1:
        val += int(vals[1])

print('\n'.join(''.join('#' if val else '.' for val in values[i*40:(i+1)*40]) for i in range(6)))
