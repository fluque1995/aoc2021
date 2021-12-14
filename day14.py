from collections import Counter, defaultdict


def parse_input():
    with open("inputs/day14.txt", "r") as fin:
        template = fin.readline().strip()
        fin.readline() # Empty line

        grammar =  dict(line.strip().split(' -> ') for line in fin.readlines())

    return template, grammar


# First problem can be brute forced, since 10 steps are doable in almost no
# time
def problem1():
    template, grammar = parse_input()
    last_template = template
    for _ in range(10):
        curr_template = []
        for i, letter in enumerate(last_template[:-1]):
            pair = ''.join(last_template[i:i+2])
            curr_template.append(letter)
            if pair in grammar:
                curr_template.append(grammar[pair])

        curr_template.append(last_template[-1])
        last_template = curr_template

    counter = Counter(last_template)
    return counter.most_common()[0][1] - counter.most_common()[-1][1]


# For problem 2, we need a more intelligent strategy
def problem2():
    template, grammar = parse_input()
    pairs_counter = defaultdict(int)
    letters_counter = defaultdict(int)
    for letter in template:
        letters_counter[letter] += 1
    for rhs, lhs in zip(template[:-1], template[1:]):
        pairs_counter[rhs + lhs] += 1

    for _ in range(40):
        next_pairs_counter = defaultdict(int)
        for pair in pairs_counter:
            if pair in grammar.keys():
                letter = grammar[pair]
                letters_counter[letter] += pairs_counter[pair]
                next_pairs_counter[pair[0] + letter] += pairs_counter[pair]
                next_pairs_counter[letter + pair[1]] += pairs_counter[pair]
            else:
                next_pairs_counter[pair] = pairs_counter[pair]
        pairs_counter = next_pairs_counter
    return max(letters_counter.values()) - min(letters_counter.values())


print(problem1())
print(problem2())
