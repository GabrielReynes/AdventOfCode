from sys import stdin

H, T = (0, 0), (0, 0)
visited = {T}

D = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

for line in stdin.read().strip().split('\n'):
    d_key, n = line.split()
    d = D[d_key]
    for _ in range(int(n)):
        H = (H[0] + d[0], H[1] + d[1])
        if max(abs(H[i] - T[i]) for i in range(2)) >= 2:
            T = (H[0] - d[0], H[1] - d[1])
            visited.add(T)

print(len(visited))
