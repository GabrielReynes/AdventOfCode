import math

from utils.aoc_utils import *
import re

DAY = 2
input = get_input(DAY)

m = {k: i for i, k in enumerate(["red", "green", "blue"])}


# submit(DAY, 1, sum(int(d[0]) for d in (
#     (re.search(r'\d+', l).group(), l.split(':')[1].split(';'))
#     for l in input.strip().split('\n')
# ) if all(all(int(j.split()[0]) <= 12 + m[j.split()[1]]
#              for j in s.strip().split(', ')) for s in d[1])))

def min_config(l):
    maxes = [0] * 3

    for draw in re.split(r'[;,] ', l.split(': ')[1]):
        q, c = draw.split()
        maxes[m[c]] = max(maxes[m[c]], int(q))

    return math.prod(maxes)


submit(DAY, 2, sum(map(min_config, input.strip().split('\n'))))
