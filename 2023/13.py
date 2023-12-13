from utils.aoc_utils import *

DAY = 13
input = get_input(DAY)
h_pats = tuple(b.split('\n') for b in input.strip().split('\n\n'))
v_pats = tuple([''.join(s) for s in zip(*b)] for b in h_pats)


# res = 0
# for pat in h_pats:
#     for i in range(len(pat) - 1):
#         if all(pat[i - j] == pat[i + j + 1] for j in range(min(i + 1, len(pat) - i - 1))):
#             res += 100 * (i + 1)
#
# for pat in v_pats:
#     for i in range(len(pat) - 1):
#         if all(pat[i - j] == pat[i + j + 1] for j in range(min(i + 1, len(pat) - i - 1))):
#             res += i + 1
#
# submit(DAY, 1, res)

def dist(str_a, str_b):
    return sum(str_a[i] != str_b[i] for i in range(len(str_a)))


res = 0
for pat in h_pats:
    for i in range(len(pat) - 1):
        if 1 == sum(dist(pat[i - j], pat[i + j + 1])
                    for j in range(min(i + 1, len(pat) - i - 1))):
            res += 100 * (i + 1)

for pat in v_pats:
    for i in range(len(pat) - 1):
        if 1 == sum(dist(pat[i - j], pat[i + j + 1])
                    for j in range(min(i + 1, len(pat) - i - 1))):
            res += i + 1

submit(DAY, 2, res)
