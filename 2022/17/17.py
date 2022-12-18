from utils.aoc_utils import *

DAY = 17

jets = tuple(1 if c == '>' else -1 for c in get_input(DAY).strip().replace('&gt;', '>').replace('&lt;', '<'))

rocks = [
    (0, 1, 2, 3),  # -
    (1, 1j, 1 + 1j, 2 + 1j, 1 + 2j),  # +
    (0, 1, 2, 2 + 1j, 2 + 2j),  # _|
    (0, 1j, 2j, 3j),  # |
    (0, 1, 1j, 1 + 1j)  # #
]

tower = set()


def update(r, o, j):
    while True:
        n_origin = o + jets[j]
        j = (j + 1) % len(jets)

        if all(next_coords not in tower and 0 <= next_coords.real < 7
               for next_coords in (coords + n_origin for coords in r)):
            o = n_origin

        n_origin = o - 1j
        if any(next_coords in tower or next_coords.imag < 1
               for next_coords in (coords + n_origin for coords in r)):
            tower.update(coords + o for coords in r)
            break
        o = n_origin
    return j


highest = 0
j_idx = 0
for r in range(2022):
    j_idx = update(rocks[r % len(rocks)], 2 + (highest + 4) * 1j, j_idx)
    highest = max(coords.imag for coords in tower)

submit(DAY, 1, highest)

# PART 2

NB_ITER = 1000000000000

tower = set()
highest = 0
j_idx = 0
last_height = 0
height_deltas = []
start_height, start_length, pattern_height, pattern_length = 0, 0, 0, 0

for r in range(NB_ITER):
    r_idx = r % len(rocks)

    if r_idx == 0:
        height_deltas.append(highest - last_height)
        last_height = highest

        found = False
        for i in range(4, len(height_deltas) // 2 + 1):
            if height_deltas[-i:] == height_deltas[-2 * i:-i]:
                start_length = len(height_deltas) - 2 * i
                start_height = sum(height_deltas[:start_length])
                pattern_length = i * len(rocks)
                pattern_height = sum(height_deltas[-i:])
                found = True
                break
        if found:
            break

    j_idx = update(rocks[r_idx], 2 + (highest + 4) * 1j, j_idx)
    highest = max(coords.imag for coords in tower)

NB_ITER -= (start_length - 1) * len(rocks)
n_highest = highest
for r in range(NB_ITER % pattern_length):
    j_idx = update(rocks[r % len(rocks)], 2 + (n_highest + 4) * 1j, j_idx)
    n_highest = max(coords.imag for coords in tower)

res = int(int(n_highest - highest + start_height + pattern_height * (NB_ITER // pattern_length)))
submit(DAY, 2, res)
