from sys import stdin
import re

starting, procedure = stdin.read().split('\n\n')

arr = list(map(lambda l: ''.join(l).lstrip(),
               zip(*map(lambda s: [s[i] for i in range(1, len(s), 4)], starting.split('\n')[:-1]))))

for p in procedure.rstrip('\n').split('\n'):
    nb, _from, to = map(int, re.search(r"move (\d+) from (\d+) to (\d+)", p).groups())
    _from -= 1
    to -= 1
    take = arr[_from][:nb][::-1]
    arr[_from] = arr[_from][nb:]
    arr[to] = take + arr[to]

print(''.join(stack[0] for stack in arr if stack))
