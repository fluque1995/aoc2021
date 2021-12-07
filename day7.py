import numpy as np


def problem1():
    with open("inputs/day7.txt", "r") as fin:
        values = list(map(int, fin.readline().strip().split(",")))

    # Best assignment in this problem is placed at the median
    median_val = np.median(values)
    fuel = np.abs(values - median_val).sum()
    return fuel


def problem2():
    with open("inputs/day7.txt", "r") as fin:
        values = np.array(list(map(int, fin.readline().strip().split(","))))

    # Best assignment in this case is around the mean. We calculate the two
    # assignments (by flooring and ceiling and keep the best)
    mean_floor = int(np.floor(np.mean(values)))
    mean_ceil = int(np.ceil(np.mean(values)))
    diff_floor = np.abs(values - mean_floor)
    diff_ceil = np.abs(values - mean_ceil)

    floor_fuel, ceil_fuel = 0, 0
    for d_f, d_c in zip(diff_floor, diff_ceil):
        floor_fuel += d_f*(d_f + 1) / 2
        ceil_fuel += d_c*(d_c + 1) / 2

    return min(floor_fuel, ceil_fuel)


print(problem1())
print(problem2())
