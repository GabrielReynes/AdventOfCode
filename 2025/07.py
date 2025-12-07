from utils.aoc_utils import read_input, submit
from collections import defaultdict

DAY = 7
YEAR = 2025

input = read_input()
# input = """.......S.......
# ...............
# .......^.......
# ...............
# ......^.^......
# ...............
# .....^.^.^.....
# ...............
# ....^.^...^....
# ...............
# ...^.^...^.^...
# ...............
# ..^...^.....^..
# ...............
# .^.^.^.^.^...^.
# ..............."""

def part1(input:str): 
    lines = input.splitlines()
    
    H = len(lines)
    S = lines[0].find('S')
    
    res = 0
    stack = [S]
    y = 1
    
    while y < H:
        nstack = set()
        while stack:
            x = stack.pop()
            if (lines[y][x] == '^') :
                res += 1
                nstack.update((x-1, x+1))
            else :
                nstack.add(x)
            
        y += 1
        stack = list(nstack)
    return res
    
        
def part2(input:str): 
    lines = input.splitlines()
    
    H = len(lines)
    S = lines[0].find('S')
    
    stack = [(S, 1)]
    y = 1
    
    while y < H:
        nstack : defaultdict[int, int] = defaultdict(int)
        while stack:
            x, count = stack.pop()
            if (lines[y][x] == '^') :
                nstack[x-1] += count
                nstack[x+1] += count
            else :
                nstack[x] += count
            
        y += 1
        stack = [(k, v) for k, v in nstack.items()]
    return sum(v for _, v in stack)


submit(part2(input), 2, YEAR, DAY)