from utils.aoc_utils import *
from collections import deque
from math import prod, lcm

DAY = 20
input = get_input(DAY).replace('&gt;', '>').replace('&amp;', '&')

d = {(n[1:] if n[0] in '%&' else n): (n[0] == '&', n[0] == '%', t.split(', '))
     for n, t in (l.split(' -> ')
                  for l in input.strip().split('\n'))}


# states = {k: False if ff else {ik: False for ik, (_, _, targets) in d.items() if k in targets}
#           for k, (con, ff, _) in d.items() if con or ff}

# lh = [0, 0]
# for i in range(1000):
#     lh[0] += 1
#     stack = deque([('broadcaster', False)])
#     while stack:
#         n, high = stack.pop()
#         targets = d[n][2]
#
#         lh[high] += len(targets)
#
#         for t in targets:
#             if t not in d:
#                 continue
#
#             con, ff, _ = d[t]
#
#             if not (con or ff):
#                 stack.appendleft((t, high))
#                 continue
#
#             if ff and not high:
#                 sends = not states[t]
#                 states[t] = sends
#                 stack.appendleft((t, sends))
#
#             if con:
#                 states[t][n] = high
#                 sends = not all(states[t].values())
#                 stack.appendleft((t, sends))
#
# submit(DAY, 1, prod(lh))

def sim(module, high_signal):
    states = {k: False if ff else {ik: False
                                   for ik, (_, _, targets) in d.items() if k in targets}
              for k, (con, ff, _) in d.items() if con or ff}
    i = 1
    while True:
        stack = deque([('broadcaster', False)])
        while stack:
            n, high = stack.pop()
            if n == module and high == high_signal:
                return i

            for t in d[n][2]:
                if t not in d:
                    continue

                con, ff, _ = d[t]

                if not (con or ff):
                    stack.appendleft((t, high))
                    continue

                if ff and not high:
                    sends = not states[t]
                    states[t] = sends
                    stack.appendleft((t, sends))

                if con:
                    states[t][n] = high
                    sends = not all(states[t].values())
                    stack.appendleft((t, sends))
        i += 1


def min_until_sent(module, high_signal):
    con = d[module][0]
    if con and not high_signal:
        return lcm(*(min_until_sent(t, True)
                     for t, (_, _, targets) in d.items() if module in targets))
    return sim(module, high_signal)


submit(DAY, 2, min(min_until_sent(t, False)
        for t, (_, _, targets) in d.items() if 'rx' in targets))
