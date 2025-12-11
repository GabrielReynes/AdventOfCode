from utils.aoc_utils import read_input, submit
import heapq

DAY = 5
YEAR = 2025

input = read_input()
# input = """3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32"""


def part1(input: str):
    ranges, ids = map(str.splitlines, input.split("\n\n"))

    rangesi = tuple(tuple(map(int, r.split("-"))) for r in ranges)

    res = sum(any(s <= int(id) <= e for s, e in rangesi) for id in ids)

    return res


def part2(input: str):
    ranges, ids = map(str.splitlines, input.split("\n\n"))

    ranges = sorted(tuple(map(int, r.split("-"))) for r in ranges)
    merged = []

    for rs, re in ranges:
        if not merged or merged[-1][1] < rs - 1:
            merged.append([rs, re])
        else:
            merged[-1][1] = max(merged[-1][1], re)

    res = sum(e - s + 1 for s, e in merged)
    return res


print(part2(input), 2, YEAR, DAY)
