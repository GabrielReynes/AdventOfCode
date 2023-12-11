from utils.aoc_utils import *
from math import lcm

DAY = 8
input = get_input(DAY)

inst, node_block = input.strip().split('\n\n')
inst = [c == 'R' for c in inst]

d = {a: b.strip('()').split(', ')
     for a, b in (l.split(' = ') for l in node_block.split('\n'))}

# act = 'AAA'
# step = 0
# while act != 'ZZZ':
#     for i in inst:
#         act = d[act][i]
#         step += 1
#
# submit(DAY, 1, step)

act = [s for s in d.keys() if s[-1] == 'A']
steps = []
for a in act:
    step = 0
    while a[-1] != 'Z':
        for i in inst:
            a = d[a][i]
            step += 1
    steps.append(step)


submit(DAY, 2, lcm(*steps))
