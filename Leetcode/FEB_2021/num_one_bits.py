def hamming_weight(n):
    return bin(n).count('1')


def hamming_weight_other(n):
    ans = 0
    while n != 0:
        n &= (n - 1)
        ans += 1
    return ans

# def check_correct(func):
#     print(func(19))
#     # assert (func(-1) == 31)
#     # print("All test cases passed")
#     return


# if __name__ == '__main__':
#     # check_correct(hamming_weight)
#     # check_correct(hamming_weight_other)
#     # print(bin(-3))
#     print(hamming_weight_other(-3))