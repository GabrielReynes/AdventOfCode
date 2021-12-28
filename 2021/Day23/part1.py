# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 10:18:53 2021

@author: Gabri
"""
import heapq
from collections import defaultdict

ROW_LENGTH = 2  # 4 for part2
lines = open('input.txt', 'r').readlines()

length = len(lines[1].strip('\n#'))
rows = ((ord(c) - ord('A') + 1 for c in line.strip('#\n ').split('#')) for line in lines[-ROW_LENGTH-1:-1])

costs = [0, 1, 10, 100, 1000]

steps = [(0, 4, [False] * length, list(zip(*rows)))]
SEEN = defaultdict(list)
result = float('inf')

while steps:
    cost, left, positions, s_block = heapq.heappop(steps)
    while True:
        p = 0
        while p < length:
            frog = positions[p]
            starter = frog * 2
            end_block = s_block[frog - 1]
            step = (starter > p) * 2 - 1
            if (positions[p] and all(f == frog for f in end_block)
                    and not any(positions[i] for i in range(p + step, starter, step))):
                cost += costs[frog] * (abs(starter - p) + ROW_LENGTH - len(end_block))
                left -= len(end_block) == (ROW_LENGTH-1)
                positions[p] = False
                s_block[frog - 1] = (frog,) + end_block
                p = -1
            p += 1
        for s in range(4):
            if all(f == s + 1 for f in s_block[s]):
                continue
            frog = s_block[s][0]
            start = (s + 1) * 2
            end = frog * 2
            end_block = s_block[frog - 1]
            if (all(f == frog for f in end_block)
                    and not any(positions[i] for i in range(start, end, (end > start) * 2 - 1))):
                cost += costs[frog] * (2*ROW_LENGTH+1 - len(end_block) - len(s_block[s]) + abs(start - end))
                left -= len(end_block) == (ROW_LENGTH-1)
                s_block[s] = s_block[s][1:]
                s_block[frog - 1] = (frog,) + end_block
                break
        else:
            break

    if not left or cost > result:
        result = min(result, cost)
        continue

    for s in range(4):
        if all(f == s + 1 for f in s_block[s]):
            continue
        pos = (s + 1) * 2
        frog = s_block[s][0]
        min_pos = max((p for p in range(pos) if positions[p]), default=-1) + 1
        max_pos = min((p for p in range(pos + 1, length) if positions[p]), default=length)
        for p in range(min_pos, max_pos):
            if p in (2, 4, 6, 8):
                continue
            n_cost = cost + costs[frog] * (ROW_LENGTH+1 - len(s_block[s]) + abs(pos - p))
            n_pos = list(positions)
            n_pos[p] = frog
            n_s_block = list(s_block)
            n_s_block[s] = s_block[s][1:]
            if not any(state == (n_pos, n_s_block) for state in SEEN[n_cost]):
                heapq.heappush(steps, (n_cost, left, n_pos, n_s_block))
                SEEN[n_cost].append((n_pos, n_s_block))

print(result)
