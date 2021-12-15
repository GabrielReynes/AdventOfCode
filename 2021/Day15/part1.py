# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:40:26 2021

@author: Gabri
"""
import heapq

MAP = list(map(lambda s: list(map(int, s.strip())), open('input.txt','r').readlines()))

width, height = len(MAP[0]), len(MAP)

SEEN = {(0, 0)}
heap = [(0, (0, 0))]

while True:
    score, (x, y) = heapq.heappop(heap)
    if x == width -1 and y == height -1:
        break
    
    for i,j in ((1,0), (-1,0), (0,1), (0,-1)):
        nx, ny = x+i, y+j
        
        if nx<0 or nx == width or ny<0 or ny  == height or (nx, ny) in SEEN: 
            continue
        
        SEEN.add((nx,ny))
        heapq.heappush(heap, (score+MAP[ny][nx], (nx, ny)))
        
print(score)