from utils.aoc_utils import *

DAY = 15
input = get_input(DAY)

strs = input.replace('\n', '').split(',')


# res = 0
# for s in strs:
#     a = 0
#     for c in s:
#         a = ((a + ord(c)) * 17) & 255
#     res += a

# submit(DAY, 1, res)

def hash(s):
    a = 0
    for c in s:
        a = ((a + ord(c)) * 17) & 255
    return a


B = [[] for _ in range(256)]

res = 0
for s in strs:

    if '-' in s:
        lab = s[:-1]
        h = hash(lab)
        B[h] = [l for l in B[h] if l[0] != lab]
    else:
        lab, l = s.split('=')
        h = hash(lab)
        for i in range(len(B[h])):
            bl, bn = B[h][i]
            if bl == lab:
                B[h][i] = (lab, l)
                break
        else:
            B[h].append((lab, l))

submit(DAY, 2, sum((hash(lab)+1) * int(l) * (i+1) for b in B for i, (lab, l) in enumerate(b)))
