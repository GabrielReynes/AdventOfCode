from utils.aoc_utils import read_input, submit
import heapq

DAY = 4
YEAR = 2025

input = read_input()
# input = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@."""

def part1(input:str): 
    rolls_map = input.splitlines()
    res = 0
    roll_char = '@'
    
    H, W = len(rolls_map), len(rolls_map[0])
    
    for y, rolls in enumerate(rolls_map):
        for x, r in enumerate(rolls):
            if r != roll_char:
                continue
            
            count = sum(0 <= x+dx < W and 0 <= y+dy < H \
                and rolls_map[y+dy][x+dx] == roll_char \
                for dx in (-1, 0, 1) for dy in (-1, 0, 1))
            
            if count < 5:
                res += 1

    return res
        

def part2(input:str):
    rolls_map = list(map(list, input.splitlines()))
    res = 0
    roll_char = '@'
    empty_char = '.'
    
    H, W = len(rolls_map), len(rolls_map[0])
    
    while True:
        prev_res = res
        for y, rolls in enumerate(rolls_map):
            for x, r in enumerate(rolls):
                if r != roll_char:
                    continue
                
                count = sum(0 <= x+dx < W and 0 <= y+dy < H \
                    and rolls_map[y+dy][x+dx] == roll_char \
                    for dx in (-1, 0, 1) for dy in (-1, 0, 1))
                
                if count < 5:
                    rolls_map[y][x] = empty_char
                    res += 1
                    
        if res == prev_res:
            break

    return res


submit(part2(input), 2, YEAR, DAY)