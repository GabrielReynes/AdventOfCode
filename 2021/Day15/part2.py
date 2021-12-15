# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 10:21:14 2021

@author: Gabri
"""

import heapq

MAP = list(map(lambda s: list(map(int, s.strip())),
           open('input.txt', 'r').readlines()))

width, height = len(MAP[0]), len(MAP)
f_width, f_height = 5*width, 5*height

SEEN = {(0, 0)}
heap = [(0, (0, 0))]

while True:
    score, (x, y) = heapq.heappop(heap)
    if x == f_width - 1 and y == f_height - 1:
        break

    for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x+i, y+j

        if nx < 0 or nx == f_width or ny < 0 or ny == f_height or (nx, ny) in SEEN:
            continue

        SEEN.add((nx, ny))
        n_risk = (MAP[ny % height][nx % width] +
                  nx//width + ny//height - 1) % 9 + 1
        heapq.heappush(heap, (score + n_risk, (nx, ny)))

print(score)
