from utils.aoc_utils import *
import re
from functools import lru_cache
from collections import defaultdict

DAY = 16

valves = {name: (i, int(rate), links.split(', ')) for i, (name, rate, links) in
          enumerate(re.match(r'Valve (.+) has flow rate=(\d+); tunnels? leads? to valves? (.+)', line).groups()
                    for line in get_input(DAY).strip().split('\n'))}


@lru_cache(maxsize=None)
def distance(f, t):
    bfs = [f]
    d = 0
    while True:
        n_bfs = []
        for v in bfs:
            if v == t:
                return d
            n_bfs.extend(valves[v][2])
        bfs = n_bfs
        d += 1


stack = [(0, 30, 'AA', 0)]
max_released = 0

while stack:
    released, time, at, opened = stack.pop()

    max_released = max(max_released, released)

    for valve, (i, rate, links) in valves.items():
        if not rate or opened & (1 << i):
            continue

        dist = distance(at, valve)
        if dist < time:
            n_time = (time - dist - 1)
            stack.append((released + rate * n_time, n_time, valve, opened | (1 << i)))

submit(DAY, 1, max_released)

# PART 2

stack = [(0, 26, 'AA', 0)]
max_released = 0
d = defaultdict(int)

while stack:
    released, time, at, opened = stack.pop()

    d[opened] = max(d[opened], released)
    max_released = max(max_released, max(released + opp for k, opp in d.items() if not (opened & k)))

    for valve, (i, rate, links) in valves.items():
        if not rate or opened & (1 << i):
            continue

        dist = distance(at, valve)
        if dist < time:
            n_time = (time - dist - 1)
            stack.append((released + rate * n_time, n_time, valve, opened | (1 << i)))

submit(DAY, 2, max_released)
