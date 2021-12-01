# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 08:29:48 2021

@author: Gabri
"""

lines = list(map(int, open("input.txt").readlines()))
print(sum(sum(lines[i:i+3]) < sum(lines[i+1:i+4]) for i in range(len(lines)-3)))