import math
from sys import stdin

lines = tuple(map(lambda l: tuple(map(int, l)), stdin.read().strip().split('\n')))
W, H = len(lines[0]), len(lines)


def ray(x, y):
    def func(args):
        dx, dy = args
        height = lines[y][x]
        length = W - x if dx > 0 else x+1 if dx < 0 else H - y if dy > 0 else y+1
        for i in range(1, length):
            if lines[y + dy * i][x + dx * i] >= height:
                return i
        return length-1

    return func


dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

print(max(math.prod(map(ray(x, y), dirs)) for x in range(1, W - 1) for y in range(1, H - 1)))
