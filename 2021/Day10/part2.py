# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 11:14:56 2021

@author: Gabri
"""
SCORES = []

O = ['(', '[', '{', '<']
C = [')', ']', '}', '>']

for l in open('input.txt', 'r').readlines():
    pile = []
    for c in l.strip():
        if c in O:
            pile.append(c)
        elif pile.pop() != O[C.index(c)]:
            break
    else:
        score = 0
        while pile:
            score = 5*score + O.index(pile.pop()) + 1
        SCORES.append(score)

print(sorted(SCORES)[len(SCORES)//2])
