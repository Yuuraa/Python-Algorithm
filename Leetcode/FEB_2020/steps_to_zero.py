def num_steps(num):
    bin_str = bin(num)[2:]
    return len(bin_str) + bin_str.count('1') - 1


def num_steps_other(num):
    steps = 0
    while num:
        num = num & 1 if num & 1 else num >> 1
        steps += 1

    return steps