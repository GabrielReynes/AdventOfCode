import heapq
import math
from sys import stdin


def monkey(description):
    lines = description.split('\n')
    return (
        list(map(int, lines[1].split(':')[1].split(','))),
        lines[2].split('=')[1].strip(),
    ) + tuple(map(int, (lines[i].split()[-1] for i in range(3, 6))))


monkeys = tuple(map(monkey, stdin.read().strip().split('\n\n')))
inspections = [0] * len(monkeys)

for _ in range(20):
    for i, (items, update, divisor, true_idx, false_idx) in enumerate(monkeys):
        inspections[i] += len(items)
        while items:
            old = items.pop()
            new = eval(update) // 3
            idx = true_idx if new % divisor == 0 else false_idx
            monkeys[idx][0].append(new)

print(math.prod(heapq.nlargest(2, inspections)))
