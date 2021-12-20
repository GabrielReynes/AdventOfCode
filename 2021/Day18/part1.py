# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 10:29:39 2021

@author: Gabri
"""
f = open('input.txt', 'r')


def to_list(string, depth=0):
    lst = []
    for c in string:
        if c in '[],':
            depth += '],['.index(c)-1
        else:
            lst.append((int(c), depth))
    return lst


values = to_list(next(f).strip())

for l in f:
    values = [(v, d+1) for v, d in values] + to_list(l.strip(), 1)

    while True:
        i = 0
        while i < len(values):
            v, d = values[i]
            if d == 5:
                if i > 0:
                    values[i-1] = (values[i-1][0]+v, values[i-1][1])
                if i+2 < len(values):
                    values[i+2] = (values[i+2][0]+values[i+1]
                                   [0], values[i+2][1])
                values[i] = (0, d-1)
                del values[i+1]
            i += 1

        for i in range(len(values)):
            v, d = values[i]
            if v > 9:
                values[i] = (v//2, d+1)
                values.insert(i+1, (v//2 + v % 2, d+1))
                break
        else:
            break

depths = [False] * 4
mag = 0
for v, d in values:
    fac = 1
    for index in range(d):
        fac *= 3 - depths[index]
    while depths[d-1]:
        depths[d-1] = False
        d -= 1
    depths[d-1] = True
    mag += fac * v

print(mag)
