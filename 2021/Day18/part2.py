# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 00:14:27 2021

@author: Gabri
"""
from itertools import permutations

lines = open('input.txt', 'r').readlines()


def to_list(string, depth=0):
    lst = []
    for c in string:
        if c in '[],':
            depth += '],['.index(c)-1
        else:
            lst.append((int(c), depth))
    return lst


def reduce(values):
    i = 0
    while True:
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
                if d == 4:
                    break
        else:
            break


def mag(values):
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
    return mag


def mag_of_couple(couple):
    values = to_list(f'[{couple[0].strip()},{couple[1].strip()}]')
    reduce(values)
    return mag(values)


print(max(map(mag_of_couple, permutations(lines, 2))))
