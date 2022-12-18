from utils.aoc_utils import *
from operator import itemgetter as ig

DAY = 18

coords = set(tuple(map(int, line.split(','))) for line in get_input(DAY).strip().split('\n'))

offsets = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

submit(DAY, 1, sum(1 for neighbors in
                   (tuple(c[i] + o[i] for i in range(3)) for c in coords for o in offsets) if
                   neighbors not in coords))

# PART 2

MIN = tuple(min(map(ig(i), coords)) - 1 for i in range(3))
MAX = tuple(max(map(ig(i), coords)) + 1 for i in range(3))

dfs = [MIN]
seen = set()
count = 0

while dfs:
    c = dfs.pop()

    if c in seen:
        continue

    seen.add(c)

    for offset in offsets:
        neighbor = tuple(c[i] + offset[i] for i in range(3))

        if not all(MIN[i] <= neighbor[i] <= MAX[i] for i in range(3)):
            continue

        if neighbor in coords:
            count += 1
        else:
            dfs.append(neighbor)

submit(DAY, 2, count)
