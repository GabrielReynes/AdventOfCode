from sys import stdin

print(sum(map(lambda t: t[1] * 3 + (t[0] + t[1] - 1) % 3 + 1,
              map(lambda t: (ord(t[0]) - ord('A'), ord(t[1]) - ord('X')),
                  (s.split() for s in stdin.read().rstrip('\n').split('\n'))))))
