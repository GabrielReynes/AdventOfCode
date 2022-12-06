from sys import stdin

minI = 0
d = dict()

for i, c in enumerate(stdin.read()):
    minI = max(minI, d.get(c, -1) + 14)
    if i >= minI:
        break
    d[c] = i

print(i + 1)
