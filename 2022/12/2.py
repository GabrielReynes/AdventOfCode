from sys import stdin
from collections import deque

S, E = None, None

MAP = [[ord(c) if c.islower() else (S := (x, y)) if c == 'S' else (E := (x, y)) for x, c in enumerate(line)]
       for y, line in enumerate(stdin.read().strip().split('\n'))]

MAP[S[1]][S[0]] = ord('a')
MAP[E[1]][E[0]] = ord('z')

W, H = len(MAP[0]), len(MAP)

stack = deque([(0, E)])
seen = set()

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while stack:
    i, coords = stack.pop()
    x, y = coords
    height = MAP[y][x]

    if height == ord('a'):
        break

    if coords in seen:
        continue

    seen.add(coords)

    for d in dirs:
        nx, ny = x + d[0], y + d[1]

        if 0 <= nx < W and 0 <= ny < H and height - MAP[ny][nx] < 2:
            stack.appendleft((i+1, (nx, ny)))

print(i)
