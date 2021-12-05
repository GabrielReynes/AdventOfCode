# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 09:43:49 2021

@author: Gabri
"""

lines = open("input.txt", 'r').readlines()
oxy = lines
co2 = lines

index = 0


def bit_count(lst): return lambda v: [t[index] for t in lst].count(v)


while len(oxy) > 1 or len(co2) > 1:
    if len(oxy) > 1:
        recOxy = max(['1', '0'], key=bit_count(oxy))
        oxy = [v for v in oxy if v[index] == recOxy]

    if len(co2) > 1:
        recCo2 = min(['0', '1'], key=bit_count(co2))
        co2 = [v for v in co2 if v[index] == recCo2]

    index += 1

print(int(oxy[0], 2) * int(co2[0], 2))
