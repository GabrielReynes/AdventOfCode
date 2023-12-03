from utils.aoc_utils import *
from collections import defaultdict

DAY = 3
input = get_input(DAY)

m = input.strip().split("\n")
W = len(m[0])
H = len(m)
m = ['.' * (W + 2)] + [f'.{l}.' for l in m] + ['.' * (W + 2)]

# def is_symbol(x, y):
#     return m[y][x] != '.'
#
#
# def is_valid(ex, l, y):
#     return (is_symbol(ex + 1, y) or is_symbol(ex - l, y) or
#             any(is_symbol(ex - l + dx, y + dy)
#                 for dx in range(l + 2)
#                 for dy in (-1, 1)))
#
#
# r = 0
# for y in range(1, H + 1):
#     s = m[y]
#     ds = ''
#     for x in range(1, W + 2):
#         c = s[x]
#         if c.isdigit():
#             ds += c
#         elif ds:
#             if is_valid(x - 1, len(ds), y):
#                 r += int(ds)
#             ds = ''
#
# submit(DAY, 1, r)

gears = defaultdict(lambda: (0, 1))

def check_gear(x, y, v):
    if m[y][x] == '*':
        a, r = gears[(x, y)]
        gears[(x, y)] = (a + 1, r * v)


def check_gears(ex, l, y, v):
    check_gear(ex + 1, y, v)
    check_gear(ex - l, y, v)
    for dy in (-1, 1):
        for dx in range(l + 2):
            check_gear(ex - l + dx, y + dy, v)


r = 0
for y in range(1, H + 1):
    s = m[y]
    ds = ''
    for x in range(1, W + 2):
        c = s[x]
        if c.isdigit():
            ds += c
        elif ds:
            check_gears(x-1, len(ds), y, int(ds))
            ds = ''

submit(DAY, 2, sum(r for a, r in gears.values() if a == 2))
