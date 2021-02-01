def concatenate_binary(n):
    result, modulus = 0, 10**9 + 7
    for num in range(1, n + 1):
        result = (result * (1 << (len(bin(num)) - 2)) + num) % modulus
    return result


def concatenate_binary_time_exception(n):
    result, len_str = 0, 0
    for num in range(n, 0, -1):
        bin_str = bin(num)[2:]
        result += num << len_str
        len_str += len(bin_str)
        result = result % (int(1e9) + 7)
  
    return result


if __name__ == "__main__":
    assert(concatenate_binary(3) == 27)
    assert(concatenate_binary(1) == 1)
    assert (concatenate_binary(12) == 505379714)

    print("All testcases passed")