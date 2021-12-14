# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 08:18:06 2021

@author: Gabri
"""
from collections import Counter

f = open('input.txt')
starter = f.readline().strip()
f.readline() #blank

counter = Counter(starter)
act = list(map(lambda i: tuple(starter[i:i+2]), range(len(starter)-1)))
dic = {tuple(k.strip()): v.strip()for k, v in map(lambda s: s.split('->'), f)}

for _ in range(10):
    new = []
    while act:
        a, b = act.pop()
        add = dic[(a, b)]
        new += [(a, add), (add, b)]
        counter[add] += 1
    act = new

values = counter.values()
print(max(values)-min(values))
