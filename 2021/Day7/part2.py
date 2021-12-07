# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 08:56:03 2021

@author: Gabri
"""

lst = tuple(map(int, open('input.txt', 'r').readline().split(',')))
mean = sum(lst)/len(lst)  # assuming that sum(lst)%len(lst) != 0
mean += sum(v - int(mean) for v in lst if v > mean) > sum(int(mean)+1 - v for v in lst if v < mean)
print(sum(abs(v-int(mean))*(abs(v-int(mean))+1)//2 for v in lst))
