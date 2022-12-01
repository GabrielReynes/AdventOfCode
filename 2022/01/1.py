from sys import stdin

print(max(sum(map(int, l.split('\n'))) for l in stdin.read().rstrip('\n').split('\n\n')))
