# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 11:25:02 2021

@author: Gabri
"""

tab = [0] * 9

for i in map(int, open('input.txt', 'r').readline().split(',')):
    tab[i] += 1

for _ in range(256):
    zero = tab[0]
    for i in range(8):
        tab[i] = tab[i+1]
    tab[6] += zero
    tab[8] = zero

print(sum(tab))
