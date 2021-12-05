# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 12:21:08 2021

@author: Gabri
"""

lines = open('input.txt', 'r').readlines()

tab = [[0] * 1000 for _ in range(1000)]
count = 0

for l in lines:
    (sX, sY), (eX, eY) = map(lambda s: map(int, s.split(',')), l.split('->'))

    dX, dY = eX - sX, eY - sY
    xP, yP = max(-1, min(1, dX)), max(-1, min(1, dY))
    dist = (abs(dX) + abs(dY)) // (abs(xP) + abs(yP))

    for i in range(dist + 1):
        x, y = sX + xP * i, sY + yP * i
        tab[x][y] += 1
        if tab[x][y] == 2:
            count += 1

print(count)
