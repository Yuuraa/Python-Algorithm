def reordered_power_of_2_old(n):
    sorted_digits = sorted(list(str(n)))
    n_max = int(''.join(sorted_digits[::-1])) # 주어진 숫자를 이용해 만들 수 있는 최댓값
    n_pow = 0

    while n_max // 2 > 0: # 최댓값의 범위 안에 드는 2의 제곱수를 구함
        n_max //= 2
        n_pow += 1
    
    for p in range(n_pow + 1):
        if sorted(list(str((1<<p)))) == sorted_digits:
            return True

    return False

def reordered_power_of_2(n):
    sorted_digits = sorted(list(str(n)))
    n_max = int(''.join(sorted_digits[::-1])) # 주어진 숫자를 이용해 만들 수 있는 최댓값
    
    num = 1
    while num <= n_max:
        if sorted(list(str(num))) == sorted_digits:
            return True
        num <<= 1

    return False


from collections import Counter
def reordered_power_of_2_other(n):
    count = collections.Counter(str(n))
    return any(count == collections.Counter(str(1<<b)) for b in xrange(31))




if __name__ == "__main__":
    assert(reordered_power_of_2(1) == True)
    assert(reordered_power_of_2(10) == False)
    assert(reordered_power_of_2(16) == True)
    assert(reordered_power_of_2(24) == False)
    assert(reordered_power_of_2(46) == True)
    assert(reordered_power_of_2(821) == True)
    print("All examples passed")