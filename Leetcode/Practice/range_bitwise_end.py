def range_bitwise_and(m, n):
    bitwise = bin(m)[2:]
    len_bits = len(bitwise)
    diff = n - m
    ans = 0

    for i in range(len_bits, 0, -1):
        if bitwise[len_bits - i] == '0': continue
        else:
            if (1 << i) - m % (1 << i) > diff:
                ans += 1 << (i-1)
    return ans


if __name__ == "__main__":
    assert(range_bitwise_and(5, 7) == 4)
    assert(range_bitwise_and(0, 1) == 0)
    assert(range_bitwise_and(3, 4) == 0)
    assert(range_bitwise_and(6, 7) == 6)
    print("All examples passed") 