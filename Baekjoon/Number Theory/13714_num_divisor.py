from collections import defaultdict

a, b, c = list(map(int, input().split()))
a, b, c = sorted([a, b, c])

n_divisors = {1: 1}
factorized_nums = {1: {}}


def calc_n_divisors(factorized_primes):
    cnt = 1
    for v in factorized_primes.values():
        cnt = cnt * (v + 1)
    cnt = cnt % (2**30)
    return cnt


def factorize(x):
    temp = x
    primes = defaultdict(int)
    for i in range(2, x+1):
        if temp in factorized_nums:
            break
        while temp % i == 0:
            temp = temp // i
            primes[i] += 1
            if temp in factorized_nums:
                break
    for k, v in factorized_nums[temp].items():
        primes[k] += v
    factorized_nums[x] = primes
    n_divisor = calc_n_divisors(primes)
    n_divisors[x] = n_divisor
    return n_divisor


def get_n_divisor(x):
    if x in n_divisors:
        return n_divisors[x]
    else:
        return factorize(x)

def get_mult_divisor(a, x):
    assert(a in factorized_nums and x in factorized_nums)
    if a*x not in n_divisors:
        primes = defaultdict(int)
        for num in [a, x]:
            for k, v in factorized_nums:
                primes[k] += v
        factorized_nums[a*x] = primes
        n_divisors[a*x] = calc_n_divisors(primes)
    return n_divisors[a*x]

