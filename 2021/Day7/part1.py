# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 07:19:52 2021

@author: Gabri
"""

lst = sorted(map(int, open('test_input.txt','r').readline().split(',')))
print(sum(abs(v-lst[len(lst)//2]) for v in lst))