from sys import stdin

lines = tuple(map(lambda l: tuple(map(int, l)), stdin.read().strip().split('\n')))
W, H = len(lines[0]), len(lines)
visible = [[False] * W for _ in range(H)]

for y, line in enumerate(lines):
    mx = -1
    for x, height in enumerate(line):
        if height > mx:
            visible[y][x] = True
            mx = height
    mx = -1
    for x, height in enumerate(line[::-1]):
        if height > mx:
            visible[y][W - 1 - x] = True
            mx = height

for x, line in enumerate(zip(*lines)):
    my = -1
    for y, height in enumerate(line):
        if height > my:
            visible[y][x] = True
            my = height
    my = -1
    for y, height in enumerate(line[::-1]):
        if height > my:
            visible[H - 1 - y][x] = True
            my = height

print(sum(map(sum, visible)))
