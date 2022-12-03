from sys import stdin

print(sum(map(lambda c: ord(c) + 1 - (ord('a') if ord(c) > ord('Z') else ord('A') - 26),
              map(lambda s: set(s[:len(s) >> 1]).intersection(set(s[len(s) >> 1:])).pop(),
                  stdin.read().rstrip('\n').split('\n')))))

