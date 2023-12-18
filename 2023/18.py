from utils.aoc_utils import *

DAY = 18
O = {'R': 'D', 'D': 'L', 'L': 'U', 'U': 'R'}
D = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
input = [(r, int(d), c.strip('()#')) for r, d, c in
         (l.split() for l in get_input(DAY).strip().split('\n'))]

# coords = (0, 0)
# area = 0
# for i in range(len(input)):
#     dir, dr, _ = input[i]
#     p_dir = input[i-1][0]
#     n_dir = input[i+1-len(input)][0]
#     p_conv = O[p_dir] == dir
#     n_conv = O[dir] == n_dir
#     dr += 1 if p_conv and n_conv else 0 if p_conv or n_conv else -1
#     dx, dy = D[dir]
#     x1, y1 = coords
#     n_coords = (x1 + dx * dr, y1 + dy * dr)
#     area += x1 * n_coords[1] - y1 * n_coords[0]
#     coords = n_coords
#
# submit(DAY, 1, abs(area) // 2)

h2d = ['R', 'D', 'L', 'U']

coords = (0, 0)
area = 0
for i in range(len(input)):
    hex = input[i][2]

    dr = int(hex[:5], 16)
    dir = h2d[int(hex[-1])]

    p_dir = h2d[int(input[i - 1][2][-1])]
    n_dir = h2d[int(input[i + 1 - len(input)][2][-1])]

    p_conv = O[p_dir] == dir
    n_conv = O[dir] == n_dir
    dr += 1 if p_conv and n_conv else 0 if p_conv or n_conv else -1
    dx, dy = D[dir]
    x1, y1 = coords
    n_coords = (x1 + dx * dr, y1 + dy * dr)
    area += x1 * n_coords[1] - y1 * n_coords[0]
    coords = n_coords

submit(DAY, 2, abs(area) // 2)
