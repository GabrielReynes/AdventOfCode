# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 12:08:48 2021

@author: Gabri
"""
import re


line = open('input.txt', 'r').readline()
match = re.search('x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)', line)
x_min, x_max, y_min, y_max = map(int, match.groups())

shots = (x_max-x_min+1)*(y_max-y_min+1)

min_vel_x = 0
while (min_vel_x + 1) * min_vel_x < 2 * x_min:
    min_vel_x += 1

max_vel_x = x_max
while max_vel_x * 2 - 1 > x_max:
    max_vel_x -= 1

max_vel_y = -y_min-1
min_vel_y = y_max+1

for vel_x in range(min_vel_x, max_vel_x+1):
    for vel_y in range(min_vel_y, max_vel_y+1):
        x, y = vel_x, vel_y
        i = 1
        while x <= x_max and y >= y_min:
            if x >= x_min and y <= y_max:
                shots += 1
                break
            x += max(0, vel_x - i)
            y += vel_y - i
            i += 1

print(shots)
