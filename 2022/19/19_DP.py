from utils.aoc_utils import *
import re
import math
from collections import Counter
import time
now = time.time()

DAY = 19

rgx = r"Blueprint \d+: Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. " \
      r"Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."

line1 = "Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. " \
        "Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian."
line2 = "Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. " \
        "Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."

blueprints = tuple(map(lambda line: tuple(map(int, re.match(rgx, line).groups())), line1.strip().split('\n')))

# For each robots -> [(blueprint_value_index, stock_index)), ...]
needs = (
    ((0, 0),),  # ore
    ((1, 0),),  # clay
    ((2, 0), (3, 1)),  # obs
    ((4, 0), (5, 2))  # geo
)

