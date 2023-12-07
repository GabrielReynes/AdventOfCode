from collections import Counter
from functools import cmp_to_key

from utils.aoc_utils import *

DAY = 7
input = get_input(DAY)

d = {c: i for i, c in enumerate('23456789TJQKA')}
counters = [(Counter(h), h, int(i))
            for h, i in (l.split() for l in input.strip().split('\n'))]


def high_card(sx, sy):
    for i, c in enumerate(sx):
        dp = d[c] - d[sy[i]]
        if dp != 0:
            return dp
    return 0


def comp(x, y):
    cx, sx, _ = x
    cy, sy, _ = y

    return len(cy) - len(cx) or max(cx.values()) - max(cy.values()) or high_card(sx, sy)


counters.sort(key=cmp_to_key(comp))

submit(DAY, 1, sum(c[2] * (i + 1) for i, c in enumerate(counters)))


# PART 2

def n_counter(h):
    c = Counter(h)
    if 'J' in c:
        nj = c['J']
        del c['J']
        mc = c.most_common(1)
        c[mc[0][0] if mc else '2'] += nj
    return c


d = {c: i for i, c in enumerate('J23456789TQKA')}
counters = [(n_counter(h), h, int(i))
            for h, i in (l.split() for l in input.strip().split('\n'))]

counters.sort(key=cmp_to_key(comp))

submit(DAY, 2, sum(c[2] * (i + 1) for i, c in enumerate(counters)))
