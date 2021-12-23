# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 05:49:10 2021

@author: Gabri
"""
import re

c = dict()

f = open('test_input.txt', 'r')


def scaled_range(s, e):
    return range(max(-50, s), min(50, e)+1)


for l in f.readlines():
    match = re.match(
        '(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)', l)
    on = match.groups()[0] == 'on'
    x1, x2, y1, y2, z1, z2 = map(int, match.groups()[1:])
    for x in scaled_range(x1, x2):
        for y in scaled_range(y1, y2):
            for z in scaled_range(z1, z2):
                c[(x, y, z)] = on


print(sum(c.values()))
