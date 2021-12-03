# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 17:38:56 2021

@author: Gabri
"""

lines = list(map(lambda l: tuple(l.split()),
             open("input.txt", 'r').readlines()))
hor = sum(int(u) for c, u in lines if c == 'forward')
dep = sum((['up', 'down'].index(c)*2-1) * int(u)
          for c, u in lines if c != 'forward')
print(hor * dep)
