def parse_input():
    with open("inputs/day8.txt", "r") as fin:
        patterns, outputs = [], []
        for line in fin.readlines():
            pattern, output = line.strip().split(" | ")
            patterns.append([set(elem) for elem in pattern.split(" ")])
            outputs.append([set(elem) for elem in output.split(" ")])

    return patterns, outputs


def problem1():
    _, outputs = parse_input()
    counter = 0
    for out_list in outputs:
        for digit in out_list:
            if len(digit) in [2, 3, 4, 7]:
                counter += 1

    return counter


def decode_input(inputs):
    # Comma means UNPACKING SHENANIGANS
    # We can determine the digits with unique number of lit segments
    digit_1, = [elem for elem in inputs if len(elem) == 2]
    digit_4, = [elem for elem in inputs if len(elem) == 4]
    digit_7, = [elem for elem in inputs if len(elem) == 3]
    digit_8, = [elem for elem in inputs if len(elem) == 7]

    # Now we can determine the six segment digits
    six_segment_digits = [elem for elem in inputs if len(elem) == 6]
    digit_9, = [elem for elem in six_segment_digits if len(elem - digit_4) == 2]
    digit_0, = [elem for elem in six_segment_digits if len(digit_1 - elem) == 0
                and elem != digit_9]
    digit_6, = [elem for elem in six_segment_digits if len(digit_1 - elem) == 1]

    # Finally, we can decode the five segment digits
    five_segment_digits = [elem for elem in inputs if len(elem) == 5]
    digit_3, = [elem for elem in five_segment_digits if len(elem - digit_7) == 2]
    digit_2, = [elem for elem in five_segment_digits if len(elem - digit_6) == 1
                and elem != digit_3]
    digit_5, = [elem for elem in five_segment_digits if len(elem - digit_6) == 0]

    return (digit_0, digit_1, digit_2, digit_3, digit_4,
            digit_5, digit_6, digit_7, digit_8, digit_9)


def decode_output(outs, in_segments):
    value = 0
    for i, output in enumerate(reversed(outs)):
        value += in_segments.index(output) * 10**i
    return value


def problem2():
    inputs, outputs = parse_input()
    value = 0
    for ins, outs in zip(inputs, outputs):
        digits = decode_input(ins)
        value += decode_output(outs, digits)

    return value


print(problem1())
print(problem2())
