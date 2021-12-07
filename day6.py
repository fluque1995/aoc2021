import numpy as np
import time


# First part of the problem is small enough to be simulated entirely. For second
# part, however, bruteforcing the result is too slow to be considered a good
# solution
def problem1():
    with open("inputs/day6.txt", "r") as fin:
        info = list(map(int, fin.readline().strip().split(",")))

    for day in range(80):
        to_add = 0
        for i, elem in enumerate(info):
            if info[i] == 0:
                to_add += 1
                info[i] = 6
            else:
                info[i] -= 1

        info.extend([8]*to_add)

    return len(info)


# Solution using Leslie matrices (https://en.wikipedia.org/wiki/Leslie_matrix)
def problem2():
    with open("inputs/day6.txt", "r") as fin:
        info = list(map(int, fin.readline().strip().split(",")))

    distrib_vector = [0]*9
    for idx, pop in zip(*np.unique(info, return_counts=True)):
        distrib_vector[8-idx] = pop

    leslie_mat = np.array(
        [[0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0]]
    )

    evolution_mat = np.linalg.matrix_power(leslie_mat, 256)
    offspring = evolution_mat.dot(distrib_vector)

    return offspring.sum()


p1_start = time.time()
p1 = problem1()
p1_end = time.time()

p2_start = time.time()
p2 = problem2()
p2_end = time.time()

print(f"Problem 1, value: {p1}, time: {p1_end - p1_start}")
print(f"Problem 2, value: {p2}, time: {p2_end - p2_start}")
