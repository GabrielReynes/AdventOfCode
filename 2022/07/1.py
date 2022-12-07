from sys import stdin

at_most = 100_000
path = []
dir_sizes = []

for line in stdin.readlines():
    match line.split():
        case ['$', 'ls'] | ['dir', _]:
            continue
        case ['$', _, '..']:
            dir_sizes.append(path.pop())
        case ['$', _, *file]:
            path.append(0)
        case [size, _]:
            for i in range(len(path)):
                path[i] += int(size)

dir_sizes.extend(path)

print(sum(s for s in dir_sizes if s <= at_most))
