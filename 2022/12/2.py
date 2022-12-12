from collections import deque
from utils import aoc_utils

DAY = 12

S, E = None, None

MAP = [[ord(c) - ord('a') if c.islower() else (S := (x, y)) if c == 'S' else (E := (x, y))
        for x, c in enumerate(line)]
       for y, line in enumerate(aoc_utils.get_input(12).strip().split('\n'))]

MAP[S[1]][S[0]] = 0
MAP[E[1]][E[0]] = 25

W, H = len(MAP[0]), len(MAP)

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

stack = deque([(0, S)])
seen = set()

while stack:
    i, coords = stack.pop()

    if coords == E:
        break

    if coords in seen:
        continue

    seen.add(coords)
    x, y = coords
    height = MAP[y][x]

    for d in dirs:
        nx, ny = x + d[0], y + d[1]

        if 0 <= nx < W and 0 <= ny < H and MAP[ny][nx] - height < 2:
            stack.appendleft((i + 1, (nx, ny)))

print(i)
aoc_utils.submit(DAY, 1, i)

# PART 2

stack = deque([(0, E)])
seen = set()

while stack:
    i, coords = stack.pop()
    x, y = coords
    height = MAP[y][x]

    if height == 0:
        break

    if coords in seen:
        continue

    seen.add(coords)

    for d in dirs:
        nx, ny = x + d[0], y + d[1]

        if 0 <= nx < W and 0 <= ny < H and height - MAP[ny][nx] < 2:
            stack.appendleft((i + 1, (nx, ny)))

print(i)
aoc_utils.submit(DAY, 2, i)
