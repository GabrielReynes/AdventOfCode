from utils.aoc_utils import *

DAY = 5
input = get_input(DAY)

blocks = input.strip().split('\n\n')
seeds = blocks[0].split(': ')[1].split()
maps = [[list(map(int, l.split()))
         for l in b.split('\n')[1:]] for b in blocks[1:]]

# tmp = list(map(int, seeds))
#
# for map in maps:
#     for i in range(len(tmp)):
#         for t, s, l in map:
#             shift = tmp[i] - s
#             if 0 < shift < l:
#                 tmp[i] = t + shift
#                 break
#
#
# submit(DAY, 1, min(tmp))


tmp = list(map(int, seeds))

for _map in maps:
    n_tmp = []
    for i in range(0, len(tmp), 2):
        ranges = [(tmp[i], tmp[i + 1], 0)]
        while ranges:
            n_ranges = []
            for ts, tl, smi in ranges:
                for mi in range(smi, len(_map)):
                    t, s, l = _map[mi]
                    ns = max(s, ts)
                    ne = min(s + l, ts + tl)
                    if ns < ne:
                        n_tmp.append(t + ns - s)
                        n_tmp.append(ne - ns)
                        if ns > ts:
                            n_ranges.append((ts, ns - ts, mi + 1))
                        if ne < ts + tl:
                            n_ranges.append((ne, ts + tl - ne, mi + 1))
                        break
                else:
                    n_tmp.append(ts)
                    n_tmp.append(tl)
            ranges = n_ranges
    tmp = n_tmp

print(DAY, 2, min(tmp[::2]))
