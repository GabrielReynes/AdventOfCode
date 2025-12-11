from utils.aoc_utils import read_input, submit
from collections import deque
from fractions import Fraction

DAY = 10
YEAR = 2025

input = read_input()
# input = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""


def part1(input: str):
    lines = input.splitlines()

    res = 0

    for l in lines:
        s_lights, *s_buttons, _ = l.split()

        target = [c == "#" for c in s_lights[1:-1]]
        buttons = tuple(tuple(map(int, b[1:-1].split(","))) for b in s_buttons)

        q = deque()
        q.append(
            (
                [
                    False,
                ]
                * len(target),
                0,
            )
        )

        while True:
            state, score = q.popleft()

            for b in buttons:
                n_state = state[:]
                for i in b:
                    n_state[i] = not n_state[i]

                if n_state == target:
                    res += score + 1
                    break
                else:
                    q.append((n_state, score + 1))
            else:
                continue
            break

    return res


def gauss_jordan_solve(moves, target):
    move_count = len(moves)
    dim_count = len(target)

    matrix = []
    for r in range(dim_count):
        row = [Fraction(m[r]) for m in moves] + [Fraction(target[r])]
        matrix.append(row)

    pivots = []
    free_vars = []

    current_row = 0
    col_to_row = {}

    for col in range(move_count):
        if current_row >= dim_count:
            free_vars.append(col)
            continue

        pivot_row = -1
        for r in range(current_row, dim_count):
            if matrix[r][col] != 0:
                pivot_row = r
                break
        else:
            free_vars.append(col)
            continue

        matrix[current_row], matrix[pivot_row] = matrix[pivot_row], matrix[current_row]

        pivot_val = matrix[current_row][col]
        for c in range(col, move_count + 1):
            matrix[current_row][c] /= pivot_val

        for r in range(dim_count):
            if r != current_row and matrix[r][col] != 0:
                factor = matrix[r][col]
                for c in range(col, move_count + 1):
                    matrix[r][c] -= factor * matrix[current_row][c]

        pivots.append(col)
        col_to_row[col] = current_row
        current_row += 1

    free_var_bounds = [
        min(
            (target[d] // moves[fv][d] for d in range(dim_count) if moves[fv][d] > 0),
            default=float("inf"),
        )
        for fv in free_vars
    ]

    best_total = float("inf")

    current_vals = [0] * len(free_vars)

    while True:
        current_free_vals = dict(zip(free_vars, current_vals))

        temp_solution = [0] * move_count

        for fv, val in current_free_vals.items():
            temp_solution[fv] = val

        valid = True

        for p in pivots:
            row_idx = col_to_row[p]

            val = matrix[row_idx][-1]

            for fv in free_vars:
                coeff = matrix[row_idx][fv]
                if coeff != 0:
                    val -= coeff * current_free_vals[fv]

            if val < 0 or val.denominator != 1:
                valid = False
                break

            temp_solution[p] = val.numerator

        if valid:
            total = sum(temp_solution)
            if total < best_total:
                best_total = total
                print("NEW BEST", best_total)

        if not free_vars:
            break

        idx = len(free_vars) - 1
        while idx >= 0:
            if current_vals[idx] < free_var_bounds[idx]:
                current_vals[idx] += 1
                break
            else:
                current_vals[idx] = 0
                idx -= 1
        else:
            break

    return best_total


def part2(input: str):
    lines = input.splitlines()

    res = 0

    for l in lines:
        _, *s_buttons, s_jolts = l.split()

        target = tuple(map(int, s_jolts[1:-1].split(",")))
        print("TARGET", target)
        buttons = sorted(
            (tuple(map(int, b[1:-1].split(","))) for b in s_buttons),
            key=lambda x: len(x),
            reverse=True,
        )
        moves = tuple(tuple(int(i in b) for i in range(len(target))) for b in buttons)
        print("BUTTONS", buttons)

        res += gauss_jordan_solve(moves, target)

    return res


print(part2(input), 2, YEAR, DAY)
