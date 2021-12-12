import numpy as np


def parse_input():
    with open("inputs/day11.txt", "r") as fin:
        values = [list(map(int, line.strip())) for line in fin.readlines()]

    values = np.array(values)
    return values, np.zeros_like(values)


def flash(flash_board, values_board, i, j):
    flash_board[i, j] = 1
    for k in [-1, 0, 1]:
        for l in [-1, 0, 1]:
            if (not (k == 0 and l == 0) and
                0 <= i+k < values_board.shape[0] and
                0 <= j+l < values_board.shape[1] and
                values_board[i+k, j+l] < 10):
                values_board[i+k, j+l] += 1
    return flash_board, values_board


def problem1():
    values, flashes = parse_input()
    counter = 0
    for _ in range(100):
        values += 1
        curr_flashes = (values == 10) * (1-flashes)
        flashes_idx = np.argwhere(curr_flashes)
        while curr_flashes.any():
            for x, y in flashes_idx:
                flashes, values = flash(flashes, values, x, y)
            curr_flashes = (values == 10) * (1-flashes)
            flashes_idx = np.argwhere(curr_flashes)

        counter += flashes.sum()
        flashes = np.zeros_like(values)
        values[values == 10] = 0

    return counter


def problem2():
    values, flashes = parse_input()
    counter, sync = 0, 0
    while sync == 0:
        counter += 1
        values += 1
        curr_flashes = (values == 10) * (1-flashes)
        flashes_idx = np.argwhere(curr_flashes)
        while curr_flashes.any():
            for x, y in flashes_idx:
                flashes, values = flash(flashes, values, x, y)
            curr_flashes = (values == 10) * (1-flashes)
            flashes_idx = np.argwhere(curr_flashes)

        if flashes.all():
            sync = counter

        flashes = np.zeros_like(values)
        values[values == 10] = 0

    return counter


print(problem1())
print(problem2())
