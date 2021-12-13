# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 08:56:03 2021

@author: Gabri
"""
lst = tuple(map(int, open('input.txt', 'r').readline().split(',')))
suite = lambda n:n*(n+1)//2
mean = sum(lst) / len(lst)
nb_inf = sum(v < mean for v in lst)
mean += len(lst)*(mean - int(mean)) > nb_inf
print(sum(suite(abs(v-int(mean))) for v in lst))