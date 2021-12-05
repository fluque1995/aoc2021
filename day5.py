import numpy as np

from collections import namedtuple
from enum import Enum

Segment = namedtuple("Segment", ["x1", "y1", "x2", "y2"])


def parse_input():
    segments = []
    max_x, max_y = 0, 0
    with open("inputs/day5.txt", "r") as fin:
        for line in fin.readlines():
            p1, p2 = line.strip().split(" -> ")
            x1, y1 = map(int, p1.split(","))
            x2, y2 = map(int, p2.split(","))
            max_x = max_x if max_x > x1 else x1
            max_x = max_x if max_x > x2 else x2
            max_y = max_y if max_y > y1 else y1
            max_y = max_y if max_y > y2 else y2
            if x2 < x1:
                x1, x2, y1, y2 = x2, x1, y2, y1
            segments.append(Segment(x1, y1, x2, y2))
    return segments, max_x+1, max_y+1


class LineType(Enum):
    HORIZONTAL = 1
    UPSIDE_VERTICAL = 2
    DOWNSIDE_VERTICAL = 3
    UPSIDE_DIAGONAL = 4
    DOWNSIDE_DIAGONAL = 5
    OTHER = 6


def line_type(segment: Segment) -> LineType:
    if segment.y1 == segment.y2:
        return LineType.HORIZONTAL
    if segment.x1 == segment.x2:
        if segment.y1 < segment.y2:
            return LineType.DOWNSIDE_VERTICAL
        else:
            return LineType.UPSIDE_VERTICAL
    if (segment.x2 - segment.x1) == (segment.y2 - segment.y1):
        return LineType.DOWNSIDE_DIAGONAL
    if (segment.x2 - segment.x1) == (segment.y1 - segment.y2):
        return LineType.UPSIDE_DIAGONAL

    return LineType.OTHER


def problem1():
    segments, max_x, max_y = parse_input()
    board = np.zeros((max_x, max_y))

    for segment in segments:
        if line_type(segment) == LineType.HORIZONTAL:
            for i in range(segment.x1, segment.x2 + 1):
                board[i, segment.y1] += 1
        if line_type(segment) == LineType.DOWNSIDE_VERTICAL:
            for i in range(segment.y1, segment.y2 + 1):
                board[segment.x1, i] += 1
        if line_type(segment) == LineType.UPSIDE_VERTICAL:
            for i in range(segment.y2, segment.y1 + 1):
                board[segment.x1, i] += 1

    return (board > 1).sum()


def problem2():
    segments, max_x, max_y = parse_input()
    board = np.zeros((max_x, max_y))
    for segment in segments:
        if line_type(segment) == LineType.HORIZONTAL:
            for i in range(segment.x1, segment.x2 + 1):
                board[i, segment.y1] += 1
        if line_type(segment) == LineType.DOWNSIDE_VERTICAL:
            for i in range(segment.y1, segment.y2 + 1):
                board[segment.x1, i] += 1
        if line_type(segment) == LineType.UPSIDE_VERTICAL:
            for i in range(segment.y2, segment.y1 + 1):
                board[segment.x1, i] += 1
        if line_type(segment) == LineType.DOWNSIDE_DIAGONAL:
            for i in range(segment.x2 - segment.x1 + 1):
                board[segment.x1 + i, segment.y1 + i] += 1
        if line_type(segment) == LineType.UPSIDE_DIAGONAL:
            for i in range(segment.x2 - segment.x1 + 1):
                board[segment.x1 + i, segment.y1 - i] += 1

    return (board > 1).sum()


print(problem1())
print(problem2())
