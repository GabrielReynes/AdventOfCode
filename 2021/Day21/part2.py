counter = [1, 3, 6, 7, 6, 3, 1]
start_spaces = [int(line.strip()[-1]) for line in open('input.txt', 'r')]
dic = dict()


def rec(factor, index, spaces, scores):
    key = (index, tuple(spaces), tuple(scores))
    if key not in dic:
        dic[key] = [0, 0]
        for add, count in enumerate(counter):
            n_spaces = list(spaces)
            n_spaces[index] = (n_spaces[index] + add + 2) % 10 + 1
            n_scores = list(scores)
            n_scores[index] += n_spaces[index]
            if n_scores[index] > 20:
                res = ((i == index) * count for i in range(2))
            else:
                res = rec(count, (index + 1) % 2, n_spaces, n_scores)
            for i in range(2):
                dic[key][i] += next(res)
    return (factor * v for v in dic[key])


print(max(rec(1, 0, start_spaces, [0, 0])))
