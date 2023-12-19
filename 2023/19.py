from utils.aoc_utils import *
from math import prod

DAY = 19

input = get_input(DAY)
workflows, ratings = input.strip().split('\n\n')
workflows = {n: tuple(
    (cond, *target[0].split('<'), target[1])
    if cond == -1 else (cond, *target[0].split('>'), target[1])
    if cond == 1 else (cond, target)
    for cond, target in ((-1 if '<' in r else 1, r.split(':'))
                         if ':' in r else (0, r)
                         for r in rules.strip('}').split(',')))
    for n, rules in (l.split('{') for l in workflows.split('\n'))}
ratings = [
    {k: int(v) for k, v in (init.split('=') for init in r.strip('{}').split(','))}
    for r in ratings.split('\n')
]


# def evaluate(rating, act):
#     while True:
#         for cond, *target in act:
#             t = None
#             if cond == 0:
#                 t = target[0]
#             elif cond == 1:
#                 var, bound, t = target
#                 if rating[var] <= int(bound):
#                     continue
#             elif cond == -1:
#                 var, bound, t = target
#                 if rating[var] >= int(bound):
#                     continue
#             if t == 'A':
#                 return True
#             if t == 'R':
#                 return False
#             act = workflows[t]
#             break
#
#
# submit(DAY, 1, sum(sum(d.values()) for d in ratings if evaluate(d, workflows['in'])))

def search_target(target):
    poss = []
    for name, workflow in workflows.items():
        for i, rule in enumerate(workflow):
            if rule[-1] != target:
                continue
            if name == 'in':
                poss.append(((name, i),))
            else:
                for p in search_target(name):
                    poss.append(p + ((name, i),))
    return poss


res = 0
for constraints in search_target('A'):
    bounds = {n: [1, 4_000] for n in ('x', 'm', 'a', 's')}
    for name, sup in constraints:
        act = workflows[name]
        for i in range(sup):
            cond, *target = act[i]
            if cond == 1:
                var, bound, t = target
                bounds[var][1] = min(bounds[var][1], int(bound))
            elif cond == -1:
                var, bound, t = target
                bounds[var][0] = max(bounds[var][0], int(bound))
        cond, *target = act[sup]
        if cond == 1:
            var, bound, t = target
            bounds[var][0] = max(bounds[var][0], int(bound)+1)
        elif cond == -1:
            var, bound, t = target
            bounds[var][1] = min(bounds[var][1], int(bound)-1)
    res += prod(max(0, m_max - m_min + 1) for m_min, m_max in bounds.values())

submit(DAY, 2, res)
