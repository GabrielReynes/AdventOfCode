from sys import stdin

print(sum(map(lambda t: t[1] + 1 + (3 if t[0] == t[1] else 6 if (t[1] - t[0]) in [1, -2] else 0),
              map(lambda t: (ord(t[0]) - ord('A'), ord(t[1]) - ord('X')),
                  (s.split() for s in stdin.read().rstrip('\n').split('\n'))))))
