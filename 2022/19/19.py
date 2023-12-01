from utils.aoc_utils import *
import re
import math
from collections import defaultdict
import time

now = time.time()

DAY = 19

rgx = r"Blueprint \d+: Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. " \
      r"Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."

line1 = "Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. " \
        "Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian."
line2 = "Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. " \
        "Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."

blueprints = tuple(map(lambda line: tuple(map(int, re.match(rgx, line).groups())), get_input(DAY).strip().split('\n')))

# For each robots -> [(blueprint_value_index, stock_index)), ...]
needs = (
    ((0, 0),),  # ore
    ((1, 0),),  # clay
    ((2, 0), (3, 1)),  # obs
    ((4, 0), (5, 2))  # geo
)

res = [0] * len(blueprints)

stack = [(bp_idx, 24, (1, 0, 0, 0), (0,) * 4) for bp_idx in range(len(blueprints))]
max_seen = [[dict() for _ in range(25)] for _ in range(len(blueprints))]
max_stock = [[defaultdict(list) for _ in range(25)] for _ in range(len(blueprints))]

count = 0
while stack:
    count += 1
    bp_idx, time_left, robots, stock = stack.pop()
    bp = blueprints[bp_idx]

    f_three = robots[:3]
    mx = max_seen[bp_idx][time_left].get(f_three, 0)
    if robots[3] < mx:
        continue

    stock_list = max_stock[bp_idx][time_left][f_three]
    if robots[3] == mx:
        if any(all(stock[i] <= saved_stock[i] for i in range(len(stock))) for saved_stock in stock_list):
            continue
        stock_list.append(stock)
        stock_list[:] = [saved_stock for saved_stock in stock_list
                         if all(stock[i] <= saved_stock[i] for i in range(len(stock)))]
    else:
        max_seen[bp_idx][time_left][f_three] = robots[3]
        stock_list.clear()


    for ri, need in enumerate(needs):
        if ri != 3 and \
                robots[ri] >= max(bp[bp_value_idx]
                                  for need in needs for bp_value_idx, stock_idx in need if ri == stock_idx):
            continue

        n_stock = list(stock)
        n_robots = tuple(r + (i == ri) for i, r in enumerate(robots))

        for bp_value_idx, stock_idx in need:
            n_stock[stock_idx] -= bp[bp_value_idx]
            if not robots[stock_idx]:
                break

        else:
            tn = max((math.ceil(-s / robots[i]) for i, s in enumerate(n_stock) if s < 0), default=0) + 1
            if tn >= time_left:
                continue

            stack.append((bp_idx, time_left - tn, n_robots,
                          tuple(map(sum, zip(n_stock, (r * tn for r in robots))))))

    res[bp_idx] = max(res[bp_idx], stock[3] + robots[3] * time_left)

print(14.55013656616211, 1264721)
print(time.time() - now, count)
print(DAY, 1, sum(r * (i + 1) for i, r in enumerate(res)))
exit()

# PART 2
now = time.time()

blueprints = tuple(map(lambda line: tuple(map(int, re.match(rgx, line).groups())), get_input(DAY).strip().split('\n')))

res = [0] * len(blueprints)

stack = [(bp_idx, 32, (1, 0, 0, 0), (0,) * 4) for bp_idx in range(len(blueprints))]
max_seen = [[dict() for _ in range(33)] for _ in range(len(blueprints))]

while stack:
    bp_idx, time_left, robots, stock = stack.pop()
    bp = blueprints[bp_idx]

    if robots[3] < max_seen[bp_idx][time_left].get(robots[:3], 0):
        continue

    max_seen[bp_idx][time_left][robots[:3]] = robots[3]

    for ri, need in enumerate(needs):
        if ri != 3 and \
                robots[ri] == max(bp[bp_value_idx]
                                  for need in needs for bp_value_idx, stock_idx in need if ri == stock_idx):
            continue

        n_stock = list(stock)
        n_robots = tuple(r + (i == ri) for i, r in enumerate(robots))

        for bp_value_idx, stock_idx in need:
            n_stock[stock_idx] -= bp[bp_value_idx]
            if not robots[stock_idx]:
                break
        else:
            tn = max((math.ceil(-s / robots[i]) for i, s in enumerate(n_stock) if s < 0), default=0) + 1
            if tn >= time_left:
                continue

            stack.append((bp_idx, time_left - tn, n_robots,
                          tuple(map(sum, zip(n_stock, (r * tn for r in robots))))))

    res[bp_idx] = max(res[bp_idx], stock[3] + robots[3] * time_left)

print(time.time() - now)
print(DAY, 2, math.prod(res))
