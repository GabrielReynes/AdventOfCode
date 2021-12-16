# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 08:40:13 2021

@author: Gabri
"""


def read(it, ln):
    return ''.join(next(it) for _ in range(ln))


def read_int(it, ln):
    return int(read(it, ln), 2)


bi = bin(int(''.join(open('input.txt', 'r')), 16))[2:]
it = iter('0'*(-len(bi) % 4) + bi)

S = 0

while True:
    v = read_int(it, 3)
    t = read_int(it, 3)

    S += v
    if t == 4:
        while True:
            st = read_int(it, 5)
            if st < 16:
                break
    else:
        l = read_int(it, 1)
        n = read_int(it, 15 - 4*l)

print(S)
