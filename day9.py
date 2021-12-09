import numpy as np


def parse_input():
    with open("inputs/day9.txt", "r") as fin:
        matrix = [list(map(int, line.strip())) for line in fin.readlines()]

    return np.array(matrix)


def problem1():
    # Solution using vectorial comparisons of numpy matrices
    original_mat = parse_input()

    top_mat = np.roll(original_mat, 1, axis=0)
    top_mat[0, :] = 10
    bottom_mat = np.roll(original_mat, -1, axis=0)
    bottom_mat[-1, :] = 10
    left_mat = np.roll(original_mat, 1, axis=1)
    left_mat[:, 0] = 10
    right_mat = np.roll(original_mat, -1, axis=1)
    right_mat[:, -1] = 10

    local_minima = ((original_mat < top_mat) *
                    (original_mat < bottom_mat) *
                    (original_mat < left_mat) *
                    (original_mat < right_mat))

    return original_mat[local_minima].sum() + local_minima.sum()


def count_basin(curr_x, curr_y, curr_map_status):
    counter = 1
    curr_map_status[curr_x, curr_y] = True
    if (curr_x - 1 > 0 and not curr_map_status[curr_x - 1, curr_y]):
        counter += count_basin(curr_x - 1, curr_y, curr_map_status)
    if (curr_x + 1 < curr_map_status.shape[0] and
        not curr_map_status[curr_x + 1, curr_y]):
        counter += count_basin(curr_x + 1, curr_y, curr_map_status)
    if (curr_y - 1 > 0 and not curr_map_status[curr_x, curr_y - 1]):
        counter += count_basin(curr_x, curr_y - 1, curr_map_status)
    if (curr_y + 1 < curr_map_status.shape[1] and
        not curr_map_status[curr_x, curr_y + 1]):
        counter += count_basin(curr_x, curr_y + 1, curr_map_status)

    return counter


def problem2():
    original_mat = parse_input()
    limits = original_mat == 9

    basin_sizes = []
    for i in range(limits.shape[0]):
        for j in range(limits.shape[1]):
            if not limits[i, j]:
                basin_sizes.append(count_basin(i, j, limits))

    basin_sizes.sort(reverse=True)

    return basin_sizes[0]*basin_sizes[1]*basin_sizes[2]


print(problem1())
print(problem2())
