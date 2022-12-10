from sys import stdin

values = []
val = 1

for line in stdin.read().strip().split('\n'):
    vals = line.split()
    for i in range(len(vals)):
        values.append(val)
    if len(vals) > 1:
        val += int(vals[1])

print(sum(values[i] * (i+1) for i in range(19, 220, 40)))
