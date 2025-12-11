from utils.aoc_utils import read_input, submit
from functools import cache

DAY = 11
YEAR = 2025

input = read_input()
# input = """aaa: you hhh
# you: bbb ccc
# bbb: ddd eee
# ccc: ddd eee fff
# ddd: ggg
# eee: out
# fff: out
# ggg: out
# hhh: ccc fff iii
# iii: out"""
# input = """svr: aaa bbb
# aaa: fft
# fft: ccc
# bbb: tty
# tty: ccc
# ccc: ddd eee
# ddd: hub
# hub: fff
# eee: dac
# dac: fff
# fff: ggg hhh
# ggg: out
# hhh: out"""

def part1(input:str): 
    res = 0
    
    lines = input.splitlines()
    
    devices = {d[:-1]:o for d, *o in map(str.split, lines)}
    
    stack = ['you']
    
    while stack:
        k = stack.pop()
        if k == 'out':
            res += 1
            continue
        reach = devices[k]
        stack.extend(reach)
        
    return res
    

def part2(input:str): 
    lines = input.splitlines()
    
    devices = {d[:-1]:o for d, *o in map(str.split, lines)}
    
    @cache
    def path_count(start, end):
        if start == end :
            return 1
        
        return sum(path_count(n, end) for n in devices.get(start, []))
    
    fft2dac = path_count('fft', 'dac')
    dac2fft = path_count('dac', 'fft')
    svr2fft = path_count('svr', 'fft')
    svr2dac = path_count('svr', 'dac')
    fft2out = path_count('fft', 'out')
    dac2out = path_count('dac', 'out')
    
    return (svr2fft * fft2dac * dac2out) + (svr2dac * dac2fft * fft2out)
    
submit(part2(input), 2, YEAR, DAY)


