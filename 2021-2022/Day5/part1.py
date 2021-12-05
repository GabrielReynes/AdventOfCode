# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 11:04:22 2021

@author: Gabri
"""
from collections import Counter


lines = open('input.txt', 'r').readlines()

c = Counter()

for l in lines:
    (x1, y1), (x2, y2) = map(lambda s: map(int, s.split(',')), l.split('->'))

    if (x1 - x2) * (y1 - y2) != 0:
        continue

    dX, dY = abs(x1 - x2), abs(y1 - y2)
    xP, yP = min(1, dX), min(1, dY)
    sX, sY = min(x1, x2), min(y1, y2)

    for i in range(dX + dY + 1):
        c[(sX + xP * i, sY + yP * i)] += 1

print(sum(1 for key in c if c[key] > 1))
