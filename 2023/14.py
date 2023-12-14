from utils.aoc_utils import *

DAY = 14
input = get_input(DAY)

lines = input.strip().split('\n')
HEIGHT = len(lines)
WIDTH = len(lines[0])

# res = 0
# for y in range(HEIGHT):
#     for x in range(WIDTH):
#         if lines[y][x] != 'O':
#             continue
#
#         o_count = 0
#         fy = y
#         for dy in range(y):
#             c = lines[y - dy - 1][x]
#             if c == '#':
#                 break
#             fy = y - dy - 1
#             if c == 'O':
#                 o_count += 1
#         res += HEIGHT - (fy + o_count)
#
# submit(DAY, 1, res)

blocks = set(x + y * 1j
             for x in range(WIDTH)
             for y in range(HEIGHT) if lines[y][x] == '#')

positions = set(x + y * 1j
                for x in range(WIDTH)
                for y in range(HEIGHT) if lines[y][x] == 'O')


def new_pos(pos, s, r, b):
    o_count = 0
    n_p = pos
    while True:
        nxt = n_p + s
        if 0 <= nxt.real < WIDTH and 0 <= nxt.imag < HEIGHT and nxt not in b:
            n_p = nxt
            if n_p in r:
                o_count += 1
        else:
            break
    return n_p - s * o_count


cache = {}
mod = 0

for i in range(1, 1000000000 + 1):
    for shift in (-1j, -1, 1j, 1):
        positions = set(new_pos(p, shift, positions, blocks) for p in positions)
    t_k = tuple((x + y * 1j in positions) for x in range(WIDTH) for y in range(HEIGHT))
    if t_k in cache:
        gap = i - cache[t_k]
        mod = (1000000000 - i) % gap
        break
    else:
        cache[t_k] = i

for i in range(mod):
    for shift in (-1j, -1, 1j, 1):
        positions = set(new_pos(p, shift, positions, blocks) for p in positions)

submit(DAY, 2, sum(HEIGHT - int(p.imag) for p in positions))
