# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 10:54:57 2021

@author: Gabri
"""

from collections import defaultdict

lines = map(lambda s: s.strip().split('-'), open('input.txt', 'r').readlines())

paths = defaultdict(list)

for a,b in lines:
    paths[a].append(b)
    paths[b].append(a)
    
COUNT = 0
pile = [({'start'}, 'start', False)]

while pile:
    seen, last, doubled = pile.pop()
    for nxt in paths[last]:
        if nxt == 'end':
            COUNT += 1
            continue
        if nxt in seen:
            if doubled or nxt == 'start': continue
            pile.append((set(seen), nxt, True))
        else:
            new_set = set(seen)
            if ord(nxt[0]) >= ord('a'): new_set.add(nxt)
            pile.append((new_set, nxt, doubled))

print(COUNT)