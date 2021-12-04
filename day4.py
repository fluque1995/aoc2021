import re
import numpy as np


def parse_input():
    boards = []
    with open("inputs/day4.txt", "r") as fin:
        values = list(map(int, fin.readline()[:-1].split(",")))
        fin.readline()
        board = []
        for i, line in enumerate(fin.readlines()):
            line = re.sub(" +", " ", line.strip())
            if i % 6 != 5:
                board.append(list(map(int, line.split(" "))))
            else:
                boards.append(board)
                board = []

    return values, np.array(boards)


def problem1():
    values, boards = parse_input()
    hits = np.zeros_like(boards)
    for val in values:
        hits[boards == val] = 1
        winning_rows = np.all(hits, axis=1).max(axis=1)
        winning_cols = np.all(hits, axis=2).max(axis=1)

        if max(winning_rows) == 1:
            winning_id = np.argmax(winning_rows)
            winning_board = boards[winning_id]
            winning_values = hits[winning_id]
            winning_sum = winning_board[winning_values == False].sum()
            return winning_sum * val

        if max(winning_cols) == 1:
            winning_id = np.argmax(winning_cols)
            winning_board = boards[winning_id]
            winning_values = values[winning_id]
            winning_sum = winning_board[winning_values == False].sum()
            return winning_sum * val


def problem2():
    values, boards = parse_input()
    hits = np.zeros_like(boards)
    curr_winning_value = 0

    winners_set = set()
    for val in values:
        hits[boards == val] = 1
        winning_rows = np.all(hits, axis=1).max(axis=1)
        winning_cols = np.all(hits, axis=2).max(axis=1)
        winning_boards = set(np.argwhere(winning_rows + winning_cols).flatten())
        for winning_id in winning_boards - winners_set:
            winners_set.add(winning_id)
            winning_board = boards[winning_id]
            winning_values = hits[winning_id]
            curr_winning_value = val * winning_board[winning_values == False].sum()

    return curr_winning_value


print(problem1())
print(problem2())
