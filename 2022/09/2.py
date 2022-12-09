from sys import stdin

R = list((0, 0) for _ in range(10))
visited = set()

D = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

for line in stdin.read().strip().split('\n'):
    d_key, n = line.split()
    for _ in range(int(n)):
        R[0] = tuple(R[0][i] + D[d_key][i] for i in range(2))
        for t in range(1, len(R)):
            diff = tuple(R[t - 1][i] - R[t][i] for i in range(2))
            if max(map(abs, diff)) < 2:
                break
            app = tuple(-1 if d < 0 else 1 if d > 0 else 0 for d in diff)
            R[t] = tuple(R[t][i] + app[i] for i in range(2))
        visited.add(R[9])

print(len(visited))
