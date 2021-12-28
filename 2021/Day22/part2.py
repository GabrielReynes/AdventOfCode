# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 06:14:30 2021

@author: Gabri
"""
import re
from itertools import combinations

f = open('input.txt', 'r')

save = []
S = 0


def overlapping(x1, x2, y1, y2):
    return x1 <= y2 and y1 <= x2


def surf_overlapping(t1, t2):
    return all(overlapping(*t1[i:i+2], *t2[i:i+2]) for i in (0, 2, 4))


def size(x1, x2, y1, y2, z1, z2):
    return (x2-x1+1)*(y2-y1+1)*(z2-z1+1)


def over_surf(t1, t2):
    t_x, t_y, t_z = (sorted((*t1[i:i+2], *t2[i:i+2])) for i in (0, 2, 4))
    return (*t_x[1:3], *t_y[1:3], *t_z[1:3])


def over_surf_m(*args):
    s = over_surf(args[0], args[1])
    for i in range(2, len(args)):
        s = over_surf(s, args[i])
    return s


for l in reversed(f.readlines()):
    match = re.match("(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)", l)
    on = match.groups()[0] == 'on'
    t = tuple(map(int, match.groups()[1:]))

    if on:
        overlaps_with = [s for s in save if surf_overlapping(t, s)]
        group_size = 1
        while True:
            groups = (c for c in combinations(overlaps_with, group_size)
                      if all(surf_overlapping(*couple) for couple in combinations(c, 2)))
            surplus = sum(size(*over_surf_m(t, *c)) for c in groups)
            S += (-2*(group_size % 2)+1) * surplus
            group_size += 1
            if not surplus:
                break

        S += size(*t)

    save.append(t)

print(S)
