from utils.aoc_utils import read_input, submit

DAY = 1
YEAR = 2025

lines = read_input().splitlines()

dial = 50
count = 0

for l in lines:
    lr, amount = l[0], int(l[1:])
    new = dial + amount if lr == "R" else dial - amount
    div, mod = divmod(new, 100)
    count += (
        abs(div)
        + (new == 0)
        + (div < 0 and mod == 0 and dial != 0)
        - (div < 0 and dial == 0 and mod != 0)
    )
    dial = mod

submit(count, 2, YEAR, DAY)
