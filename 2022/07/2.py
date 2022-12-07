from sys import stdin

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


total = 70_000_000
target = 30_000_000
root_size = path[0]
min_free = target - total + root_size
dir_sizes.extend(path)

print(min(size for size in dir_sizes if size > min_free))
