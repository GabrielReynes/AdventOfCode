# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 12:21:08 2021

@author: Gabri
"""
from collections import Counter

lines = open('input.txt', 'r').readlines()

c = Counter()

for l in lines:
    (sX, sY), (eX, eY) = map(lambda s: map(int, s.split(',')), l.split('->'))

    dX, dY = eX - sX, eY - sY
    xP, yP = max(-1, min(1, dX)), max(-1, min(1, dY))

    for i in range(max(abs(dX), abs(dY)) + 1):
        c[(sX + xP * i, sY + yP * i)] += 1

print(sum(1 for key in c if c[key] > 1))
