from utils.aoc_utils import *
import re

DAY = 1

# submit(DAY, 1, sum(int(''.join((d[0], d[-1]))) for d in (
#     re.findall('\d', line) for line in get_input(DAY).strip().split('\n'))
# ))

so = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
m = {k: i + 1 for i, k in enumerate(so)}
m.update({str(i): i for i in range(1, 10)})
r = f'(?=({"|".join(so)}|\d))'

submit(DAY, 2, sum(m[d[0]] * 10 + m[d[-1]] for d in (
    re.findall(r, line) for line in get_input(DAY).strip().split('\n'))))
