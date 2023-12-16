from utils.aoc_utils import *

DAY = 16
input = get_input(DAY)

M = input.strip().split('\n')
HEIGHT = len(M)
WIDTH = len(M[0])

# stack = [(-1, 1)]
# seen = set()
#
# while stack:
#     elm = stack.pop()
#     if elm in seen:
#         continue
#     seen.add(elm)
#     c, d = elm
#     nc = c + d
#     if 0 <= nc.real < WIDTH and 0 <= nc.imag < HEIGHT:
#         char = M[int(nc.imag)][int(nc.real)]
#         if char == '.' or (d.imag == 0 and char == '-') or (d.real == 0 and char == '|'):
#             stack.append((nc, d))
#         elif char == '\\':
#             stack.append((nc, d.imag + d.real * 1j))
#         elif char == '/':
#             stack.append((nc, -d.imag - d.real * 1j))
#         elif char == '-':
#             stack.append((nc, -1))
#             stack.append((nc, 1))
#         elif char == '|':
#             stack.append((nc, 1j))
#             stack.append((nc, -1j))
#
#
# submit(DAY, 1, len(set(t[0] for t in seen)) -1)

res = 0
for sd, r in ((1, (-1 + i * 1j for i in range(HEIGHT))),
              (-1, (WIDTH + i * 1j for i in range(HEIGHT))),
              (1j, (i - 1j for i in range(WIDTH))),
              (-1j, (i + HEIGHT * 1j for i in range(WIDTH)))):
    for s in r:
        stack = [(s, sd)]
        seen = set()

        while stack:
            elm = stack.pop()
            if elm in seen:
                continue
            seen.add(elm)
            c, d = elm
            nc = c + d
            if 0 <= nc.real < WIDTH and 0 <= nc.imag < HEIGHT:
                char = M[int(nc.imag)][int(nc.real)]
                if (char == '.'
                        or (d.imag == 0 and char == '-')
                        or (d.real == 0 and char == '|')):
                    stack.append((nc, d))
                elif char == '\\':
                    stack.append((nc, d.imag + d.real * 1j))
                elif char == '/':
                    stack.append((nc, -d.imag - d.real * 1j))
                elif char == '-':
                    stack.append((nc, -1))
                    stack.append((nc, 1))
                elif char == '|':
                    stack.append((nc, 1j))
                    stack.append((nc, -1j))

        res = max(res, len(set(t[0] for t in seen)) - 1)

submit(DAY, 2, res)
