n, m = list(map(int, input().split()))

factorials = [0 for _ in range(n+1)]

def factorial(x):
    if factorials[x] != 0:
        return factorials[x]
    if x == 0 or x == 1:
        factorials[x] = 1
    else:
        factorials[x] = factorial(x-1) * x
    return factorials[x]


print(factorial(n)//(factorial(m)*factorial(n-m)))