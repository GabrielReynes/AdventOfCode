from utils.aoc_utils import *
from heapq import heappush, heappop
from collections import defaultdict

DAY = 17
input = get_input(DAY)

M = [list(map(int, l)) for l in input.strip().split('\n')]
H = len(M)
W = len(M[0])

heap = [(0, (0, 0), (1, 0), 0), (0, (0, 0), (0, 1), 0)]
cache = defaultdict(lambda: float('inf'))
m_hl = 0

# while heap:
#     hl, c, d, r = heappop(heap)
#
#     if cache[(c, d, r)] > hl:
#         cache[(c, d, r)] = hl
#     else:
#         continue
#
#     (cx, cy), (dx, dy) = c, d
#
#     if cx == (W - 1) and cy == (H - 1):
#         m_hl = hl
#         break
#
#     if r < 3:
#         nx = cx + dx
#         ny = cy + dy
#         if 0 <= nx < W and 0 <= ny < H:
#             heappush(heap, (hl + M[ny][nx], (nx, ny), (dx, dy), r + 1))
#
#     if 0 <= cx + dy < W and 0 <= cy + dx < H:
#         nx = cx + dy
#         ny = cy + dx
#         heappush(heap, (hl + M[ny][nx], (nx, ny), (dy, dx), 1))
#
#     if 0 <= cx - dy < W and 0 <= cy - dx < H:
#         nx = cx - dy
#         ny = cy - dx
#         heappush(heap, (hl + M[ny][nx], (nx, ny), (-dy, -dx), 1))
#
# submit(DAY, 1, m_hl)

while heap:
    hl, c, d, r = heappop(heap)

    if cache[(c, d, r)] > hl:
        cache[(c, d, r)] = hl
    else:
        continue

    (cx, cy), (dx, dy) = c, d

    if cx == (W - 1) and cy == (H - 1):
        if r < 4:
            continue
        m_hl = hl
        break

    if r < 10:
        nx = cx + dx
        ny = cy + dy
        if 0 <= nx < W and 0 <= ny < H:
            heappush(heap, (hl + M[ny][nx], (nx, ny), (dx, dy), r + 1))

    if r > 3:
        if 0 <= cx + dy < W and 0 <= cy + dx < H:
            nx = cx + dy
            ny = cy + dx
            heappush(heap, (hl + M[ny][nx], (nx, ny), (dy, dx), 1))

        if 0 <= cx - dy < W and 0 <= cy - dx < H:
            nx = cx - dy
            ny = cy - dx
            heappush(heap, (hl + M[ny][nx], (nx, ny), (-dy, -dx), 1))

submit(DAY, 2, m_hl)
