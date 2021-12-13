# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 12:24:17 2021

@author: Gabri
"""

f = open('input.txt')
dots = set()

for l in f:
    if l.isspace(): break
    dots.add(tuple(map(int, l.split(','))))
        
for axe, val in map(lambda s:s.split('='), f.readlines()):
    if axe[-1]=='x': 
        width = int(val)
        dots = set((a if a < width else 2*width-a, b) for a,b in dots)
    else: 
        height = int(val)
        dots = set((a, b if b < height else 2*height-b) for a,b in dots)
    
MAP = [['.'] * width for _ in range(height)]

for a,b in dots: MAP[b][a] = '#'

print(*(''.join(l) for l in MAP), sep='\n')