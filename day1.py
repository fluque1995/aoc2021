import math


def problem1():
    counter = 0
    curr = math.inf

    with open("inputs/day1.txt", "r") as data:
        for line in data.readlines():
            if curr < int(line):
                counter += 1
            curr = int(line)

    return counter


def problem2():
    counter = 0
    elems = 4*[math.inf]

    with open("inputs/day1.txt", "r") as data:
        for line in data.readlines():
            elems = elems[1:] + [int(line)]
            if elems[0] < elems[-1]:
                counter += 1

    return counter


print(problem1())
print(problem2())
