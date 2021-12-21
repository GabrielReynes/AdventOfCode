# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 15:52:41 2021

@author: Gabri
"""

f = open('input.txt', 'r')

def str_to_list(string):
    return [c == '#' for c in string.strip()]

algo = str_to_list(f.readline())
next(f)

image = list(map(str_to_list, f))
width, height = len(image[0]), len(image)

ext_val = False

def neb_to_bool(x, y, val, scale = (-1,0,1)):
    return algo[int(''.join('01'[val[x+i][y+j]] for i in scale for j in scale), 2)]

for _ in range(2): #50 for part2
    mock = [[ext_val] * (width+4), [ext_val] * (width+4)]
    for r in range(height):
        mock.append([ext_val]*2 + image[r] + [ext_val] * 2)
    mock += [[ext_val] * (width+4), [ext_val] * (width+4)]
    image = []
    for c in range(1, width+3):
        image.append([neb_to_bool(c,r,mock) for r in range(1, height+3)])
        
    width += 2
    height += 2
    ext_val = algo[511 * ext_val]
    
print(sum(sum(l) for l in image))