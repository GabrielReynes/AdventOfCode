from utils.aoc_utils import *

DAY = 4
input = get_input(DAY)

# print(DAY, 1, sum(2 ** (n - 1) if n > 0 else 0 for n in (
#     len(set(w.split()) & set(m.split()))
#     for w, m in (
#     l.split(': ')[1].split(' | ') for l in input.strip().split('\n')
# ))))

c = input.strip().split('\n')
n = [1] * len(c)

for i in range(len(c)):
    w, m = c[i].split(': ')[1].split(' | ')
    win = len(set(w.split()) & set(m.split()))
    for j in range(win):
        n[i + j + 1] += n[i]

print(DAY, 2, sum(n))
