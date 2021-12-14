# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 08:43:30 2021

@author: Gabri
"""
from collections import Counter

lines = open('input.txt').readlines()
starter = lines[0].strip()
final = Counter(starter)
counter = Counter(map(lambda i: tuple(starter[i:i+2]), range(len(starter)-1)))
dic = {tuple(k.strip()): v.strip()
       for k, v in map(lambda s: s.split('->'), lines[2:])}

for _ in range(40):
    new = Counter()
    for (a, b), v in counter.items():
        add = dic[(a, b)]
        new[(a, add)] += v
        new[(add, b)] += v
        final[add] += v
    counter = new

count = final.values()
print(max(count)-min(count))
