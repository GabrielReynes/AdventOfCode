from utils.aoc_utils import read_input, submit
from collections import defaultdict

DAY = 12
YEAR = 2025

input = read_input()
test_input = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""


def part1(input: str):
    *shape_blocks, regions_str = input.split("\n\n")
    shapes = [block.splitlines()[1:] for block in shape_blocks]

    def get_rotations(shape_idx):
        shape = shapes[shape_idx]
        base_cells = [
            (x, y)
            for y, row in enumerate(shape)
            for x, ch in enumerate(row)
            if ch == "#"
        ]
        rotations = []
        seen = set()

        for rot in range(4):
            rotated = base_cells
            for _ in range(rot):
                max_y = max(y for x, y in rotated)
                rotated = [(max_y - y, x) for x, y in rotated]

            min_x = min(x for x, y in rotated)
            min_y = min(y for x, y in rotated)
            normalized = tuple(sorted((x - min_x, y - min_y) for x, y in rotated))

            if normalized not in seen:
                seen.add(normalized)
                cells = list(normalized)
                w = max(x for x, y in cells) + 1
                h = max(y for x, y in cells) + 1
                rotations.append((cells, w, h))

        return rotations

    all_rotations = [get_rotations(i) for i in range(len(shapes))]

    placement_cache = {}

    def get_shape_placements(shape_idx, width, height):
        if width > height:
            width, height = height, width

        key = (shape_idx, width, height)
        if key in placement_cache:
            return placement_cache[key]

        placements = []
        for cells, sw, sh in all_rotations[shape_idx]:
            for py in range(height - sh + 1):
                for px in range(width - sw + 1):
                    mask = 0
                    for dx, dy in cells:
                        mask |= 1 << ((py + dy) * width + (px + dx))
                    placements.append(mask)

        placement_cache[key] = placements
        return placements

    memo_caches = defaultdict(lambda: defaultdict(dict))

    def can_tile(width, height, counts):
        if width > height:
            width, height = height, width

        total_shapes = sum(counts)

        if total_shapes == 0:
            return True

        total_cells = sum(
            len(all_rotations[si][0][0]) * cnt for si, cnt in enumerate(counts)
        )
        if total_cells > width * height:
            return False

        grid_key = (width, height)
        memo_cache = memo_caches[grid_key]

        shape_placements = [
            get_shape_placements(si, width, height) for si in range(len(counts))
        ]

        def solve(used_mask: int, remaining: tuple[int, ...]):
            mask_cache = memo_cache[used_mask]

            for r, v in mask_cache.items():
                if v and all(ra <= rb for ra, rb in zip(remaining, r)):
                    return True
                if (not v) and all(ra >= rb for ra, rb in zip(remaining, r)):
                    return False

            if all(c == 0 for c in remaining):
                return True

            best_type = -1
            best_valid = None

            for si, v in enumerate(remaining):
                if v == 0:
                    continue
                valid = [p for p in shape_placements[si] if (p & used_mask) == 0]
                if len(valid) < remaining[si]:
                    mask_cache[remaining] = False
                    return False
                best_type = si
                best_valid = valid
                break

            new_remaining = tuple(v - (i == best_type) for i, v in enumerate(remaining))

            for mask in best_valid:
                if solve(used_mask | mask, new_remaining):
                    mask_cache[remaining] = True
                    return True

            mask_cache[remaining] = False
            return False

        return solve(0, counts)

    regions = []
    for i, line in enumerate(regions_str.splitlines()):
        size, count_str = line.split(": ")
        w, h = map(int, size.split("x"))
        counts = tuple(map(int, count_str.split()))
        regions.append((i, w, h, counts))

    regions.sort(key=lambda x: (min(x[1], x[2]), max(x[1], x[2]), sum(x[3])))

    res = 0
    for idx, (i, w, h, counts) in enumerate(regions):
        res += can_tile(w, h, counts)
        if (idx + 1) % 100 == 0:
            print(f"Progress: {idx + 1}/{len(regions)}", flush=True)

    return res


print(part1(input), 1, YEAR, DAY)
