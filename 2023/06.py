from utils.aoc_utils import *
from math import prod, sqrt, ceil, floor

DAY = 6
input = get_input(DAY)

# tds = zip(*(map(int, l.split(':')[1].split())
#             for l in input.strip().split('\n')))
#
# submit(DAY, 1, prod(sum(1 for i in range(t) if (t - i) * i > d) for t, d in tds))

t, d = (int(''.join(l.split(':')[1].split())) for l in input.strip().split('\n'))

delta = sqrt(t * t - 4 * d)

submit(DAY, 2, abs(floor((t + delta) / 2) - floor((t - delta) / 2)))
