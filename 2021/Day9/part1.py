# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:05:31 2021

@author: Gabri
"""
MAP = list(map(lambda l: list(map(int, f"9{l.strip()}9")),
           open('input.txt', 'r').readlines()))

MAP = [[9]*len(MAP[0])] + MAP + [[9]*len(MAP[0])]

S = 0

for y in range(1, len(MAP)-1):
    for x in range(1, len(MAP[0])-1):
        S += (MAP[y][x]+1) * all(MAP[y+j][x+i] > MAP[y][x]
                                 for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)))

print(S)
