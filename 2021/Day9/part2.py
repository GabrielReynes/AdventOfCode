# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 18:42:09 2021

@author: Gabri
"""
MAP = list(map(lambda l: list(map(int, f"9{l.strip()}9")),
           open('input.txt', 'r').readlines()))

MAP = [[9]*len(MAP[0])] + MAP + [[9]*len(MAP[0])]

SEEN = set()


def neighbors(x, y):
    return tuple((x+i, y+j) for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)))


B = []
for y in range(1, len(MAP)-1):
    for x in range(1, len(MAP[0])-1):
        if (x, y) in SEEN:
            continue

        neb = neighbors(x, y)
        if all(MAP[j][i] > MAP[y][x] for i, j in neb):
            SEEN.update(neb)
            pile = list(neb)
            size = 0
            while pile:
                i, j = pile.pop()
                if MAP[j][i] == 9:
                    continue
                size += 1

                not_seen = tuple(n for n in neighbors(i, j) if n not in SEEN)
                pile += not_seen
                SEEN.update(not_seen)

            B.append(size)
            B = sorted(B, reverse=True)[:3]


print(B[0]*B[1]*B[2])
