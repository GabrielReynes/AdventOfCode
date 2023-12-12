from utils.aoc_utils import *
from functools import cache

DAY = 12
input = get_input(DAY)

lines = [(l, tuple(map(int, r.split(','))))
         for l, r in (l.split() for l in input.strip().split('\n'))]


@cache
def compute(pat, cond, idx, cond_idx, h_count):
    if idx == len(pat):
        return (cond_idx == len(cond) or
                cond_idx == len(cond) - 1 and h_count == cond[cond_idx])

    c = pat[idx]
    res = 0

    if c in '.?':
        res += (h_count == 0 and
                compute(pat, cond, idx + 1, cond_idx, 0) or
                (h_count != 0 and cond[cond_idx] == h_count and
                 compute(pat, cond, idx + 1, cond_idx + 1, 0)))
    if c in '#?':
        res += (cond_idx < len(cond) and
                (h_count < cond[cond_idx] and
                 compute(pat, cond, idx + 1, cond_idx, h_count + 1)))

    return res


# submit(DAY, 1, sum(compute(pat, cond, 0, 0, 0) for pat, cond in lines))

submit(DAY, 2, sum(compute('?'.join((pat,) * 5), cond * 5, 0, 0, 0)
                   for pat, cond in lines))
