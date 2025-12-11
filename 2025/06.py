from utils.aoc_utils import read_input, submit

DAY = 6
YEAR = 2025

input = read_input()
# input = """123 328  51 64
#  45 64  387 23
#   6 98  215 314
# *   +   *   +"""


def part1(input: str):
    lines = input.splitlines()

    columns = list(zip(*(l.split() for l in lines)))

    res = sum(eval(c[-1].join(c[:-1])) for c in columns)

    return res


def part2(input: str):
    lines = input.splitlines()

    columns = list(zip(*lines[:-1]))
    ops = lines[-1].split()

    grpd = [[]]
    for c in columns:
        if all(not v.strip() for v in c):
            grpd.append([])
        else:
            grpd[-1].append(c)

    res = sum(
        eval(op.join("".join(t[::-1] for t in s) for s in c))
        for c, op in zip(grpd, ops)
    )

    return res


print(part2(input), 2, YEAR, DAY)
