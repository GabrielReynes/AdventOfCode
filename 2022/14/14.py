from utils.aoc_utils import *

DAY = 14

paths = tuple(tuple(tuple(map(int, coords.split(','))) for coords in path.split('->'))
              for path in get_input(DAY).strip().split('\n'))

sand = 500

MAP = set()

for path in paths:
    for s, e in zip(path, path[1:]):
        x1, y1 = min(s, e)
        x2, y2 = max(s, e)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                MAP.add(x + y * 1j)

max_y = max(z.imag for z in MAP)
dirs = (1j, -1 + 1j, 1 + 1j)

for part in (1, 2):
    units = 0
    while True:
        units += 1
        act = sand
        while act.imag <= max_y:
            for d in dirs:
                if act + d not in MAP:
                    act += d
                    break
            else:
                break
        if part == 1 and act.imag > max_y:
            break
        if part == 2 and act == sand:
            break
        MAP.add(act)

    submit(DAY, part, units - 2 + part)
