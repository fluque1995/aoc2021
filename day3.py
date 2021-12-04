def problem1():
    with open("inputs/day3.txt", "r") as fin:
        values = fin.read().splitlines()

    accs = []
    for pos_numbers in zip(*values):
        accs.append(sum(map(int, pos_numbers)))

    maximums = map(lambda x: int((x / len(values)) > 0.5), accs)
    final_pos, final_neg = 0, 0
    for i, mult in enumerate(reversed(list(maximums))):
        final_pos += mult*2**i
        final_neg += (1-mult)*2**i

    return final_pos * final_neg


def problem2():
    with open("inputs/day3.txt", "r") as fin:
        values = fin.read().splitlines()

    integers_list = []
    for numbers in values:
        integers_list.append(list(map(int, numbers)))

    oxygen_integers_list, co2_integers_list = integers_list, integers_list

    for i in range(len(oxygen_integers_list[0])):
        curr_digits = [integer[i] for integer in oxygen_integers_list]
        curr_digits_sum = sum(curr_digits)
        oxygen_kept_value = 0 if curr_digits_sum < len(oxygen_integers_list) / 2 else 1
        oxygen_integers_list = [integer for integer in oxygen_integers_list
                                if integer[i] == oxygen_kept_value]
        if len(oxygen_integers_list) == 1:
            break

    for i in range(len(co2_integers_list[0])):
        curr_digits = [integer[i] for integer in co2_integers_list]
        curr_digits_sum = sum(curr_digits)
        co2_kept_value = 0 if curr_digits_sum >= len(co2_integers_list) / 2 else 1
        co2_integers_list = [integer for integer in co2_integers_list
                             if integer[i] == co2_kept_value]
        if len(co2_integers_list) == 1:
            break

    oxygen_bin = oxygen_integers_list[0]
    co2_bin = co2_integers_list[0]

    ox_value, co2_value = 0, 0
    for i in range(len(oxygen_bin)):
        ox_value += oxygen_bin[i]*2**(len(oxygen_bin) - i - 1)
        co2_value += co2_bin[i]*2**(len(co2_bin) - i - 1)

    return ox_value * co2_value


print(problem1())
print(problem2())
