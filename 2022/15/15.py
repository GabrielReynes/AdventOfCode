from utils.aoc_utils import *
import re

DAY = 15

check_y = 2000000

SET = set()

sensors = tuple(tuple(map(int, re.match(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)',
                                        line).groups())) for line in get_input(DAY).strip().split('\n'))

for sx, sy, bx, by in sensors:
    x_dist = abs(sx - bx)
    y_dist = abs(sy - by)
    dist = x_dist + y_dist
    check_y_dist = abs(sy - check_y)
    if check_y_dist > dist:
        continue
    delta = dist - check_y_dist
    SET.update(range(sx - delta, sx + delta))

submit(DAY, 1, len(SET))

# PART 2

MIN = 0
MAX = 4000000

x, y = MIN, MIN

while True:
    for sx, sy, bx, by in sensors:
        x_dist = abs(sx - x)
        y_dist = abs(sy - y)
        dist = x_dist + y_dist

        b_dist = abs(sx - bx) + abs(sy - by)
        if b_dist < dist:
            continue

        y = sy + b_dist - x_dist + 1
        if y > MAX:
            y = MIN
            x += 1

        break
    else:
        break

submit(DAY, 2, x * MAX + y)
