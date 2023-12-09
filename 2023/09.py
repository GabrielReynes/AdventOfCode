from utils.aoc_utils import *

DAY = 9
input = get_example(DAY)
ls = [list(map(int, l.split())) for l in input.strip().split('\n')]

# r = 0
# for l in ls:
#     while any(l):
#         r += l[-1]
#         l = [l[i+1] - l[i] for i in range(len(l)-1)]
#
#
# submit(DAY, 1, r)

r = 0
for l in ls:
    while any(l):
        print(l[0])
        r += l[0]
        l = [l[i] - l[i+1] for i in range(len(l)-1)]


submit(DAY, 2, r)
