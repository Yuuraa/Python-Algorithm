def divide_ints(dividend, divisor):
    assert(divisor != 0)
    if dividend / divisor >= 2**31 - 1:
        return 2 ** 31 - 1
    
    ans = dividend // divisor
    if dividend % divisor == 0: 
        return ans
    
    if ans < 0: ans += 1
    return ans


def divide_ints_bitwise(dividend, divisor):
    if dividend == -1<<31 and divisor == -1: return (1<<31) - 1

    a, b = abs(dividend), abs(divisor)
    sign = (dividend < 0) == (divisor < 0)
    res, cand = 0, [(1, b)]

    while b << 1 <= a:
        cand += [(cand[-1][0]<<1, b<<1)]
        b <<= 1

    for pw, num in cand[::-1]:
        if a >= num:
            a, res = a - num, res + pw
    
    return res if sign else -res


if __name__ == "__main__":
    assert(divide_ints(7, -3) == -2)
    assert(divide_ints(0, 1) == 0)
    assert(divide_ints(10, 3) == 3)
    assert(divide_ints(1, -1) == -1)
    print("All examples passed")