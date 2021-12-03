import math


def problem1():
    depth = 0
    distance = 0
    with open("inputs/day2.txt", "r") as data:
        for line in data.readlines():
            move_type, dist = line.split(" ")
            if move_type == 'up':
                depth -= int(dist)
            elif move_type == 'down':
                depth += int(dist)
            elif move_type == 'forward':
                distance += int(dist)

    return depth, distance


def problem2():
    depth = 0
    distance = 0
    aim = 0
    with open("inputs/day2.txt", "r") as data:
        for line in data.readlines():
            move_type, dist = line.split(" ")
            if move_type == 'up':
                aim -= int(dist)
            elif move_type == 'down':
                aim += int(dist)
            elif move_type == 'forward':
                distance += int(dist)
                depth += int(dist) * aim
    return depth, distance


print(f"{problem1()} - {math.prod(problem1())}")
print(f"{problem2()} - {math.prod(problem2())}")
