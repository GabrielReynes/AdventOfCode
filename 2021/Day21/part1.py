cases = [int(line.strip()[-1]) for line in open('input.txt', 'r')]
scores = [0, 0]
played = 0
while all(score < 1000 for score in scores):
    index = played % 2
    cases[index] = (cases[index] + 6 + 9 * played - 1) % 10 + 1
    scores[index] += cases[index]
    played += 1

print(min(scores) * played * 3)
