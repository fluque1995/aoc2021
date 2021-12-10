def parse_input():
    with open("inputs/day10.txt", "r") as fin:
        lines = [line.strip() for line in fin.readlines()]

    return lines


def problem1():
    symbol_failures = []
    inputs = parse_input()
    for line in inputs:
        symbols_stack = []
        for delim in line:
            if delim in '<([{':
                symbols_stack.append(delim)
            else:
                last_delim = symbols_stack.pop()
                if ((delim == '>' and last_delim != '<') or
                    (delim == ')' and last_delim != '(') or
                    (delim == ']' and last_delim != '[') or
                    (delim == '}' and last_delim != '{')):

                    symbol_failures.append(delim)
                    break

    scores_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
    return sum([scores_map[symbol] for symbol in symbol_failures])


def compute_score(remaining_tokens):
    curr_score = 0
    scores_map = {'(': 1, '[': 2, '{': 3, '<': 4}
    for symbol in reversed(remaining_tokens):
        curr_score *= 5
        curr_score += scores_map[symbol]
    return curr_score


def problem2():
    inputs = parse_input()
    incomplete_scores = []
    for line in inputs:
        incomplete_input = True
        symbols_stack = []
        for delim in line:
            if delim in '<([{':
                symbols_stack.append(delim)
            else:
                last_delim = symbols_stack.pop()
                if ((delim == '>' and last_delim != '<') or
                    (delim == ')' and last_delim != '(') or
                    (delim == ']' and last_delim != '[') or
                    (delim == '}' and last_delim != '{')):
                    incomplete_input = False
                    break
        if incomplete_input:
            incomplete_scores.append(compute_score(symbols_stack))

    incomplete_scores.sort()
    return incomplete_scores[len(incomplete_scores) // 2]


print(problem1())
print(problem2())
