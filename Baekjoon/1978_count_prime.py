n = int(input())
nums = list(map(int, input().split()))

import math
def is_prime(number):
    if number in [0, 1]:
        return False
    if number == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
    return True

prime_nums = [1 if is_prime(val) else 0 for val in nums]
print(sum(prime_nums))