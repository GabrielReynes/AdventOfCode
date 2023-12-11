from utils.aoc_utils import *
from itertools import combinations

DAY = 11
input = get_input(DAY)

lines = input.strip().split('\n')

WIDTH = len(lines[0])
HEIGHT = len(lines[0])
coords = []
empty_ys = [0]
seen_xs = set()

for y in range(HEIGHT):
    empty_line = True
    for x in range(WIDTH):
        if lines[y][x] == '#':
            coords.append((x, y))
            seen_xs.add(x)
            empty_line = False
    empty_ys.append(empty_ys[-1] + (1 if empty_line else 0))

empty_xs = [0]
for x in range(WIDTH):
    empty_xs.append(empty_xs[-1] + (0 if x in seen_xs else 1))

empty_xs.pop(0)
empty_ys.pop(0)

res = 0
for (x1, y1), (x2, y2) in combinations(coords, 2):
    res += abs(x1 - x2) + abs(y1 - y2)
    res += 999999 * (empty_xs[max(x1, x2)] - empty_xs[min(x1, x2)])
    res += 999999 * (empty_ys[max(y1, y2)] - empty_ys[min(y1, y2)])


submit(DAY, 2, int(res))
