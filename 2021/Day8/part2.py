# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 09:02:05 2021

@author: Gabri
"""
S = 0
D = {2: 1, 3: 7, 4: 4, 7: 8}
for l in open('input.txt', 'r').readlines():
    patterns, digits = l.split('|')
    known = dict()
    for p in patterns.split():
        if len(p) in D:
            known[D[len(p)]] = set(p)

    for i, d in enumerate(map(set, digits.split())):
        if len(d) == 6:
            v = 9 if known[4] <= d else 0 if known[1] <= d else 6
        elif len(d) == 5:
            v = 3 if known[1] <= d else 5 if len(known[4] & d) == 3 else 2
        else:
            v = D[len(d)]
        S += v * 10**(3-i)
print(S)
