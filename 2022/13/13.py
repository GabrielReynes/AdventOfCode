import math

from utils.aoc_utils import *
import ast

DAY = 13

pairs = tuple((tuple(map(ast.literal_eval, pair.split('\n'))) for pair in get_input(DAY).strip().split('\n\n')))


def right_order(p1, p2):
    if isinstance(p1, int):
        if isinstance(p2, int):
            return None if p1 == p2 else p1 < p2
        p1 = [p1]
    if isinstance(p2, int):
        p2 = [p2]
    for i in range(min(len(p1), len(p2))):
        res = right_order(p1[i], p2[i])
        if res is None:
            continue
        return res
    return None if len(p1) == len(p2) else len(p1) < len(p2)


submit(DAY, 1, sum(right_order(*pair) * (i + 1) for i, pair in enumerate(pairs)))

div_keys = [[[2]], [[6]]]

submit(DAY, 2, math.prod(sum(right_order(p, div_keys[i]) for pair in pairs for p in pair) + i + 1 for i in range(2)))
