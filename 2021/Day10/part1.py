# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 09:44:17 2021

@author: Gabri
"""
S = 0

P = {')': ('(', 3), ']': ('[', 57), '}': ('{', 1197), '>': ('<', 25137)}

for l in open('input.txt', 'r').readlines():
    pile = []
    for c in l:
        if c not in P:
            pile.append(c)
        else:
            if pile.pop() != P[c][0]:
                S += P[c][1]
                break
print(S)
