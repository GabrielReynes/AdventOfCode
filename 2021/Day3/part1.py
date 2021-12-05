# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 09:18:08 2021

@author: Gabri
"""

lines = open('input.txt', 'r').readlines()
res = [0] * len(lines[0])

for l in lines:
    res = (sum(v) for v in zip(res, map(int, l.strip())))

gamma = int("".join(str(round(v/len(lines))) for v in res), 2)

print(gamma * (~gamma & 0xFFF))
