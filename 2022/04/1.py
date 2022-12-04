from sys import stdin
import re

print(sum((t[0] <= t[2] and t[1] >= t[3]) or (t[2] <= t[0] and t[3] >= t[1]) for t in
          map(lambda l: tuple(map(int, re.search("(\d+)-(\d+),(\d+)-(\d+)", l).groups())),
              stdin.read().rstrip('\n').split('\n'))))
