# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 11:19:42 2021

@author: Gabri
"""
import re


line = open('input.txt', 'r').readline()
match = re.search('x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)', line)
x_min, x_max, y_min, y_max = map(int, match.groups())

max_y_vel = max(y_min, y_max, key=abs)
print(max_y_vel * (max_y_vel+1) // 2)