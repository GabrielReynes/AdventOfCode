from utils.aoc_utils import read_input, submit
import heapq

DAY = 3
YEAR = 2025

input = read_input()
# input = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111"""

def part1(input:str): 
    banks = input.splitlines()
    res = 0
    
    for b in banks:
        (v1, i1), (_, i2) = heapq.nlargest(2, ((c, i) for i,c in enumerate(b)))
        il, ig = sorted((i1, i2))
        jolt = int(f"{b[il]}{b[ig]}") if b[il] >= b[ig] or ig == (len(b)-1) \
            else int(f"{v1}{max(b[i1+1:])}")
        res += jolt
        

    return res
        

def part2(input:str):
    banks = input.splitlines()
    tl = 12
    res = 0
    
    for b in banks:
        idx = [-1]
        for t in range(0, tl): 
            lidx = idx[-1]+1
            _, i = max((c, -(i + lidx)) \
                for i, c in enumerate(b[lidx:len(b)-tl+t+1]))
            idx.append(-i)
        jolt = int("".join(b[i] for i in idx[1:]))
        res += jolt
            
    return res


print(part2(input), 2, YEAR, DAY)