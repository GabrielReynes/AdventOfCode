# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 17:24:02 2021

@author: Gabri
"""
SIZE = 5

lines = open('input.txt', 'r').readlines()

arr = {e: i for i, e in enumerate(map(int, lines[0].split(',')))}

round_min = len(arr)

for i in range(2, len(lines), SIZE+1):
    numbers = tuple(map(lambda s: tuple(map(int, s.split())), lines[i:i+SIZE]))

    min_lines = min((max(l, key=arr.get) for l in numbers), key=arr.get)
    min_colums = min((max(l, key=arr.get) for l in zip(*numbers)), key=arr.get)

    win_val = min(min_lines, min_colums, key=arr.get)
    win_round = arr[win_val]

    if round_min > win_round:
        board_sum = sum(sum(v for v in l if arr[v] > win_round) for l in numbers)
        min_sum = board_sum * win_val
        round_min = win_round

print(min_sum)
