import queue
import math


def parse_input():
    with open("inputs/day15.txt", "r") as fin:
        matrix = [list(map(int, line.strip())) for line in fin.readlines()]

    return matrix


def build_bigger_maze(maze, mult=5):
    len_x = len(maze[0])
    len_y = len(maze)
    bigger_maze = [[0]*mult*len_x for i in range(mult*len_y)]
    for i in range(len_x):
        for j in range(len_y):
            curr_val = maze[i][j]
            for k in range(mult):
                for l in range(mult):
                    bigger_maze[k*len_x+i][l*len_y+j] = (curr_val+k+l) % 9
                    if bigger_maze[k*len_x+i][l*len_y+j] == 0:
                        bigger_maze[k*len_x+i][l*len_y+j] = 9

    return bigger_maze


class Path(object):
    def __init__(self, maze, curr_pos, visited_nodes=[], curr_cost=0):
        self.visited_nodes = visited_nodes
        self.curr_cost = curr_cost
        self.curr_pos = curr_pos
        self.maze = maze

    def __str__(self):
        return (f"Visited nodes: {self.visited_nodes}\n"
                f"Current position: {self.curr_pos}\n"
                f"Current cost: {self.curr_cost}\n"
                f"Expected cost: {self.expected_cost()}\n")

    def __repr__(self):
        return self.__str__()

    def expected_cost(self):
        return (self.curr_cost
                + (len(self.maze) - self.curr_pos[0])
                + (len(self.maze[0]) - self.curr_pos[1]))

    def __lt__(self, other):
        return self.expected_cost() < other.expected_cost()

    def finished_path(self):
        return self.curr_pos == (len(self.maze[0])-1, len(self.maze)-1)

    def visitable_pos(self, pos):
        return (0 <= pos[0] < len(self.maze[0]) and
                0 <= pos[1] < len(self.maze) and
                pos not in self.visited_nodes)

    def visit_neighbors(self):
        possible_paths = []
        for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            next_pos = (self.curr_pos[0] + i, self.curr_pos[1] + j)
            if self.visitable_pos(next_pos):
                new_nodes = self.visited_nodes + [next_pos]
                new_cost = self.curr_cost + self.maze[next_pos[0]][next_pos[1]]
                possible_paths.append(
                    Path(self.maze, next_pos, new_nodes, new_cost))

        return possible_paths


class AStar(object):
    def __init__(self, maze):
        self.paths = queue.PriorityQueue()
        self.optimal_costs = [[math.inf]*len(maze[0]) for _ in range(len(maze))]
        self.paths.put(Path(maze, (0, 0), visited_nodes=[(0,0)]))

    def step(self):
        curr_path = self.paths.get()
        if curr_path.finished_path():
            return True, curr_path
        else:
            possible_paths = curr_path.visit_neighbors()
            for path in possible_paths:
                pos = path.curr_pos
                if self.optimal_costs[pos[0]][pos[1]] > path.curr_cost:
                    self.optimal_costs[pos[0]][pos[1]] = path.curr_cost
                    self.paths.put(path)

            return False, None

    def search_maze(self):
        finished, path = self.step()
        while not finished:
            finished, path = self.step()

        return path


def problem1():
    maze = parse_input()
    searcher = AStar(maze)
    output = searcher.search_maze()
    return output.curr_cost


def problem2():
    maze = parse_input()
    big_maze = build_bigger_maze(maze, 5)
    searcher = AStar(big_maze)
    output = searcher.search_maze()
    return output.curr_cost


print(problem1())
print(problem2())
