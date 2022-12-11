from heapq import nlargest
from math import prod
from sys import stdin
from operator import itemgetter


def monkey(description):
    lines = description.split('\n')
    return (
        list(map(int, lines[1].split(':')[1].split(','))),
        lines[2].split('=')[1].strip(),
    ) + tuple(map(int, (lines[i].split()[-1] for i in range(3, 6))))


monkeys = tuple(map(monkey, stdin.read().strip().split('\n\n')))
divisors = tuple(map(itemgetter(2), monkeys))
inspections = [0] * len(monkeys)

for items, *args in monkeys:
    for i, v in enumerate(items):
        items[i] = [v % d for d in divisors]

for _ in range(10_000):
    for m_idx, (items, update, divisor, true_idx, false_idx) in enumerate(monkeys):
        inspections[m_idx] += len(items)
        while items:
            remainders = items.pop()
            new = [eval(update) % divisors[i] for i, old in enumerate(remainders)]
            idx = true_idx if new[m_idx] == 0 else false_idx
            monkeys[idx][0].append(new)

print(prod(nlargest(2, inspections)))
