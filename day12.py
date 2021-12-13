import time

from collections import defaultdict


def parse_input():
    adjacency_dict = defaultdict(list)
    with open("inputs/day12.txt") as fin:
        for line in fin.readlines():
            begin, end = line.strip().split("-")
            adjacency_dict[begin].append(end)
            adjacency_dict[end].append(begin)

    return adjacency_dict


def explore_graph(curr_node,
                  target_node,
                  adj_dict,
                  visited_nodes,
                  small_cavern_twice = True):
    sols = []
    visited_nodes.append(curr_node)
    if curr_node == target_node:
        sols.append(visited_nodes)
    for node in adj_dict[curr_node]:
        if node == node.upper() or node not in visited_nodes:
            vis_nodes = visited_nodes.copy()
            sols.extend(explore_graph(
                node, target_node, adj_dict, vis_nodes, small_cavern_twice))
        elif node != 'start' and node != 'end' and not small_cavern_twice:
            vis_nodes = visited_nodes.copy()
            sols.extend(explore_graph(
                node, target_node, adj_dict, vis_nodes, True))

    return sols


def problem1():
    adjs = parse_input()
    return len(explore_graph('start', 'end', adjs, []))


def problem2():
    adjs = parse_input()
    return len(explore_graph('start', 'end', adjs, [], False))


print(problem1())
print(problem2())
