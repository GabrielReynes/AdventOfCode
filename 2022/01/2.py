from sys import stdin

print(sum(sorted(sum(map(int, l.split('\n'))) for l in stdin.read().rstrip('\n').split('\n\n'))[-3:]))
