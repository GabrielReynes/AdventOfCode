from utils.aoc_utils import read_input, submit
from itertools import combinations
from math import sqrt, prod
from heapq import nlargest

DAY = 8
YEAR = 2025

input = read_input()
# input = """162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689"""


def part1(input: str):
    def dist(a: tuple[int, ...], b: tuple[int, ...]):
        dx = b[0] - a[0]
        dy = b[1] - a[1]
        dz = b[2] - a[2]
        return sqrt(dx * dx + dy * dy + dz * dz)

    boxes = tuple(tuple(map(int, l.split(","))) for l in input.splitlines())

    pair_count = 1000
    junctions = dict[int, int]()
    jidx = 0
    b2j = dict[int, int]()
    pairs = nlargest(
        pair_count,
        (
            (-dist(a, b), ia, ib)
            for (ia, a), (ib, b) in combinations(enumerate(boxes), 2)
        ),
    )

    for _, ia, ib in pairs:
        ainj, binj = ia in b2j, ib in b2j
        if ainj:
            if binj:
                jia, jib = b2j[ia], b2j[ib]
                if jia != jib:
                    junctions[jia] += junctions.pop(jib)
                    b2j.update({k: jia for k, v in b2j.items() if v == jib})
            else:
                ji = b2j[ib] = b2j[ia]
                junctions[ji] += 1
        elif binj:
            ji = b2j[ia] = b2j[ib]
            junctions[ji] += 1
        else:
            ji = b2j[ia] = b2j[ib] = jidx
            junctions[ji] = 2
            jidx += 1

    return prod(nlargest(3, junctions.values()))


def part2(input: str):
    def dist(a: tuple[int, ...], b: tuple[int, ...]):
        dx = b[0] - a[0]
        dy = b[1] - a[1]
        dz = b[2] - a[2]
        return sqrt(dx * dx + dy * dy + dz * dz)

    boxes = tuple(tuple(map(int, l.split(","))) for l in input.splitlines())

    junctions = dict[int, int]()
    jidx = 0
    b2j = dict[int, int]()
    pairs = sorted(
        (dist(a, b), ia, ib) for (ia, a), (ib, b) in combinations(enumerate(boxes), 2)
    )

    for _, ia, ib in pairs:
        ainj, binj = ia in b2j, ib in b2j
        if ainj:
            if binj:
                jia, jib = b2j[ia], b2j[ib]
                if jia != jib:
                    junctions[jia] += junctions.pop(jib)
                    b2j.update({k: jia for k, v in b2j.items() if v == jib})
            else:
                ji = b2j[ib] = b2j[ia]
                junctions[ji] += 1
        elif binj:
            ji = b2j[ia] = b2j[ib]
            junctions[ji] += 1
        else:
            ji = b2j[ia] = b2j[ib] = jidx
            junctions[ji] = 2
            jidx += 1

        if len(junctions) == 1 and sum(junctions.values()) == len(boxes):
            return boxes[ia][0] * boxes[ib][0]

    return 0


print(part2(input), 2, YEAR, DAY)
