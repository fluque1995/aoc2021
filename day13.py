def parse_input():
    coordinates, folds = set(), []
    folding = False
    with open("inputs/day13.txt", "r") as fin:
        for line in fin.readlines():
            line = line.strip()
            if line:
                if not folding:
                    coordinates.add(tuple(int(val) for val in line.split(",")))
                else:
                    rhs, value = line.split("=")
                    folds.append((rhs.split(" ")[-1], int(value)))
            else:
                folding = True

    return coordinates, folds


def fold(coords, fold_line):
    direction, value = fold_line
    new_coords = set()
    for coord in coords:
        if fold_line[0] == 'x':
            new_coord = coord if coord[0] < fold_line[1] else (
                fold_line[1] - (coord[0] - fold_line[1]), coord[1])
        else:
            new_coord = coord if coord[1] < fold_line[1] else (
                coord[0], fold_line[1] - (coord[1] - fold_line[1]))

        new_coords.add(new_coord)

    return new_coords


def show_folding(coords_list):
    max_x, max_y = 0, 0
    for x, y in coords_list:
        if max_x < x:
            max_x = x
        if max_y < y:
            max_y = y

    matrix = [' '*(max_x+1)]*(max_y+1)
    for x, y in coords_list:
        matrix[y] = matrix[y][:x] + '#' + matrix[y][x+1:]

    for line in matrix:
        print(line)


def problem1():
    coordinates, folds = parse_input()
    return len(fold(coordinates, folds[0]))


def problem2():
    coordinates, folds = parse_input()
    for folding in folds:
        coordinates = fold(coordinates, folding)

    show_folding(coordinates)


print(problem1())
problem2()
