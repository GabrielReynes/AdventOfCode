import heapq

lines = open('input.txt', 'r').readlines()
inp_indices = (i for i in range(len(lines)) if lines[i].startswith('inp'))
inp_indices = tuple(inp_indices) + (len(lines),)

cmd = {'add': int.__add__, 'mul': int.__mul__, 'div': lambda x, y: x // y + (x ^ y < 0),
       'mod': int.__mod__, 'eql': int.__eq__}


def get_val(string):
    return idents[string] if string in idents else int(string)


SEEN = set()
heap = [(0, 0, 0, (0,) * 4)]
max_found = 0

while heap:
    z_val, mod, size, idents = heapq.heappop(heap)
    couples = tuple(zip('wxyz', idents))
    for inp_val in range(9, 0, -1):
        idents = dict(couples)
        start_index = inp_indices[size]
        idents[lines[start_index].split()[-1]] = inp_val
        for instr, ide, val in map(str.split, lines[start_index + 1:inp_indices[size + 1]]):
            idents[ide] = cmd[instr](*map(get_val, (ide, val)))
        key = tuple(idents.values())
        if key not in SEEN:
            SEEN.add(key)
            n_mod = 10 * mod + inp_val
            if size == 13:
                if not key[-1]:
                    max_found = max(max_found, n_mod)
            else:
                heapq.heappush(heap, (abs(key[-1]), n_mod, size + 1, key))

print(max_found)
