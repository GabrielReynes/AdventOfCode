from sys import stdin

print(sum(map(lambda c: ord(c) + 1 - (ord('a') if ord(c) > ord('Z') else ord('A') - 26),
              map(lambda g: set.intersection(*map(set, g)).pop(),
                  (lambda l: [l[i:i + 3] for i in range(0, len(l), 3)])(stdin.read().rstrip('\n').split('\n'))))))
