# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 17:48:39 2021

@author: Gabri
"""

lines = open("input.txt", 'r')
aim, hor, depth = 0, 0, 0
for l in lines:
    c, u = l.split()
    if c == 'forward':
        hor += int(u)
        depth += aim * int(u)
    else:
        aim += (['up', 'down'].index(c)*2-1) * int(u)
print(hor*depth)
