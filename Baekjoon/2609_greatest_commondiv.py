a, b = map(int, input().split())


def calc_gcd(a, b):
    gcd = 1
    for cd in range(2, min(a, b) + 1):
        if a % cd == 0 and b % cd == 0:
            gcd = cd

    return gcd


import math
# gcd = math.gcd(a, b)
gcd = calc_gcd(a, b)
print(gcd)
print(a*b // gcd)