# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 11:01:10 2021

@author: Gabri
"""


def prod(args):
    p = 1
    for i in args:
        p *= i
    return p


op = [sum, prod, min, max, int.__gt__, int.__lt__, int.__eq__]


def read_int(it, ln):
    return int(''.join(next(it) for _ in range(ln)), 2)


def read_lit(it):
    s = bit_length = 0
    while True:
        f = read_int(it, 1)
        n = read_int(it, 4)
        s = (s << 4) + n
        bit_length += 5
        if not f:
            break
    return s, bit_length


def read_op(it, t):
    l = read_int(it, 1)
    n = read_int(it, 15 - 4*l)

    bit_length = 16 - 4*l

    args = []
    while n > 0:
        v, size = read_val(it)

        n -= size*(not l) + l
        bit_length += size
        args.append(v)

    return op[t](args) if t < 4 else op[t-1](*args), bit_length


def read_val(it):
    v = read_int(it, 3)
    t = read_int(it, 3)

    if t == 4:
        v, size = read_lit(it)
    else:
        v, size = read_op(it, t)

    return v, size + 6


bi = bin(int(''.join(open('input.txt', 'r')), 16))[2:]
it = iter(bi.zfill(-len(bi) % 4))

v, size = read_val(it)

print(v)
