from utils.aoc_utils import *
from collections import deque

DAY = 10
input = get_input(DAY)

E, W, N, S = 1, 2, 4, 8
F = {'|': N | S, '-': E | W, 'L': N | E, 'J': N | W, '7': S | W, 'F': S | E, 'S': 0}
T = {'|': N | S, '-': E | W, 'L': S | W, 'J': S | E, '7': N | E, 'F': N | W, '.': 0, 'S': 0}
D = {S: 1j, N: -1j, W: -1, E: 1}

M = input.strip().split('\n')
WIDTH = len(M[0])
HEIGHT = len(M)
s_coords = 0

for y in range(HEIGHT):
    for x in range(WIDTH):
        if M[y][x] == 'S':
            s_coords = x + y * 1j
            for d_mask, shift in D.items():
                nc = s_coords + shift
                x = int(nc.real)
                y = int(nc.imag)
                if 0 <= x < WIDTH and 0 <= y < HEIGHT and (T[M[y][x]] & d_mask):
                    F['S'] |= d_mask
            break
    else:
        continue
    break

stack = deque([(s_coords, 0)])
seen = set()
m_max = 0
while stack:
    coord, d = stack.pop()
    if coord in seen:
        continue
    m_max = max(m_max, d)
    seen.add(coord)
    fc_mask = F[M[int(coord.imag)][int(coord.real)]]
    for d_mask, shift in D.items():
        if (d_mask & fc_mask) == 0:
            continue
        nc = coord + shift
        x = int(nc.real)
        y = int(nc.imag)
        if 0 <= x < WIDTH and 0 <= y < HEIGHT and (T[M[y][x]] & d_mask):
            stack.appendleft((nc, d + 1))

t_area = 0
for y in range(HEIGHT):
    for x in range(WIDTH):
        coord = x + y * 1j
        if coord in seen:
            continue
        inouts = 0
        on_line = False
        l_mask = 0
        while True:
            coord += 1
            if coord.real == WIDTH:
                t_area += inouts & 1
                break

            c = M[y][int(coord.real)]
            if on_line:
                on_line = c == '-'
                if not on_line and (F[c] & l_mask):
                    inouts += 1
                continue
            if coord in seen:
                mask = F[c]
                on_line = (mask & (W | E)) != 0
                l_mask = mask & (N | S)
                inouts += 1

# submit(DAY, 1, m_max)
submit(DAY, 2, t_area)
