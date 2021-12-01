# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 08:23:27 2021

@author: Gabri
"""

lines = list(map(int, open("input.txt").readlines()))
print(sum(lines[i-1] < lines[i] for i in range(1,len(lines))))