# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 08:39:47 2021

@author: Gabri
"""
lines = map(lambda s: s.split('|')[1], open('input.txt', 'r').readlines())
print(sum(sum(len(w) in {2, 3, 4, 7} for w in l.split()) for l in lines))
