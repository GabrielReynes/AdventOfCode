from utils.aoc_utils import read_input, submit
from itertools import combinations, pairwise, chain

DAY = 9
YEAR = 2025

input = read_input()
# input = """7,1
# 11,1
# 11,7
# 9,7
# 9,5
# 2,5
# 2,3
# 7,3"""


def part1(input: str):
    coords = (tuple(map(int, l.split(","))) for l in input.splitlines())
    return max(
        (abs(ax - bx) + 1) * (abs(ay - by) + 1)
        for (ax, ay), (bx, by) in combinations(coords, 2)
    )


def part2(input: str):
    vertices = [tuple(map(int, l.split(","))) for l in input.splitlines()]
    xs, ys = tuple(sorted(set(c)) for c in zip(*vertices))

    edges = list(pairwise(chain(vertices, vertices[:1])))

    def is_inside(x: int, y: int) -> int:
        cnt = sum(
            x1 == x2 and x < x1 and min(y1, y2) <= y < max(y1, y2)
            for (x1, y1), (x2, y2) in edges
        )
        return cnt & 1

    grid = [
        [is_inside((x1 + x2) // 2, (y1 + y2) // 2) for x1, x2 in pairwise(xs)]
        for y1, y2 in pairwise(ys)
    ]

    h, w = len(grid), len(grid[0])

    sum_grid = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            sum_grid[i][j] = (
                grid[i][j]
                + (sum_grid[i - 1][j] if i > 0 else 0)
                + (sum_grid[i][j - 1] if j > 0 else 0)
                - (sum_grid[i - 1][j - 1] if i > 0 and j > 0 else 0)
            )

    x_map = {x: i for i, x in enumerate(xs)}
    y_map = {y: i for i, y in enumerate(ys)}

    def get_sum(ra, ca, rb, cb):
        return (
            sum_grid[rb][cb]
            - (sum_grid[ra - 1][cb] if ra > 0 else 0)
            - (sum_grid[rb][ca - 1] if ca > 0 else 0)
            + (sum_grid[ra - 1][ca - 1] if ra > 0 and ca > 0 else 0)
        )

    max_area = 0

    for (x1, y1), (x2, y2) in combinations(vertices, 2):
        if x1 == x2 or y1 == y2:
            continue

        ix1, ix2 = sorted((x_map[x1], x_map[x2]))
        iy1, iy2 = sorted((y_map[y1], y_map[y2]))

        expctd = (ix2 - ix1) * (iy2 - iy1)

        actl = get_sum(iy1, ix1, iy2 - 1, ix2 - 1)

        if actl == expctd:
            max_area = max(max_area, (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))

    return max_area


print(part2(input), 2, YEAR, DAY)
