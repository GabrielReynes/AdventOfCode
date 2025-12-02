from utils.aoc_utils import read_input, submit

DAY = 2
YEAR = 2025

input = read_input()
# input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

def part1(input): 
    ranges = input.split(',')
    res = 0

    for r in ranges:
        s, e = r.split('-')
        
        if len(s) & 1 == 1:
            s = f"1{"0" * len(s)}"
        if len(e) & 1 == 1:
            e = "9" * (len(e) - 1)
            
        sl, sr = int(s[:len(s)>>1]), int(s[len(s)>>1:])
        el, er = int(e[:len(e)>>1]), int(e[len(e)>>1:])
        
        sl += sr > sl
        el -= er < el
        
        res += sum(int(f"{p}{p}") for p in range(sl, el+1))        
        
    return res

def part2(input:str):
    ranges = input.split(',')
    res = set()

    for r in ranges:
        s, e = r.split('-')
                
        for gs in range(1, 1 + (max(len(s), len(e)) >> 1)): 
            qs,rs = divmod(len(s), gs)
            qe,re = divmod(len(e), gs)
            
            ms = s if rs == 0 else f"1{"0" * ((gs * (qs+1)) - 1)}"
            me = e if re == 0 else "9" * (gs * qe)
            
            msl = min(int(me[:gs]), int(ms[:gs]))
            mel = int(me[:len(me) - len(ms) + gs] or "0")
            
            si, ei = int(s), int(e)
            
            inv = (int(str(l) * q) for l in range(msl, mel + 1) for q in range(max(2, qs), qe+1))
            invc = (i for i in inv if i >= si and i <= ei)
            
            res.update(invc)
            
        
    return sum(res)


print(part2(input), 2, YEAR, DAY)