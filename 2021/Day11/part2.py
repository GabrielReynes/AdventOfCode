# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 12:52:45 2021

@author: Gabri
"""

MAP = list(map(lambda s: list(map(int, s.strip())), open("input.txt", 'r').readlines()))
step = 0
while True:
    flashes = []
    flashed = set()
    for y in range(10):
        for x in range(10):
            MAP[y][x] += 1
            if MAP[y][x] > 9 :
                flashes.append((x,y))
                flashed.add((x,y))
    while flashes:
        x,y = flashes.pop()
        MAP[y][x] = 0
        for i in (-1,0,1):
            if x + i < 0 or x + i > 9: continue
            for j in (-1,0,1):
                if y + j < 0 or y + j > 9: continue
                
                if (x+i, y+j) in flashed:
                    continue
                
                MAP[y+j][x+i] += 1
                if MAP[y+j][x+i] > 9:
                    flashes.append((x+i, y+j))
                    flashed.add((x+i, y+j))
    step += 1
    if len(flashed) == 100:
        print(step)
        break