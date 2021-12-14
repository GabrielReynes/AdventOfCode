# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 08:18:06 2021

@author: Gabri
"""
from collections import Counter

lines = open('input.txt').readlines()

act = list(map(lambda i: tuple(lines[0][i:i+2]), range(len(lines[0].strip())-1)))
counter = Counter(lines[0].strip())
dic = {tuple(k.strip()) : v.strip() for k,v in map(lambda s:s.split('->'), lines[2:])}

for _ in range(10):
    new = []
    while act:
        a,b = act.pop()
        add = dic[(a,b)]
        new += [(a, add), (add, b)]
        counter[add] += 1
    act = new
        
print(max(counter.values())-min(counter.values()))