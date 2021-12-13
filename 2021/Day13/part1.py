# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 11:44:42 2021

@author: Gabri
"""

f = open('input.txt')
dots = set()

for l in f:
    if l.isspace():
        break
    dots.add(map(int, l.split(',')))

axe, val = f.readline().split('=')

if axe[-1] == 'x':
    print(len(set((a if a < int(val) else 2*int(val)-a, b) for a, b in dots)))
else:
    print(len(set((a, b if b < int(val) else 2*int(val)-b) for a, b in dots)))
