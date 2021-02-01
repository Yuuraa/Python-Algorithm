N, K = map(int, input().split())
answer = 0

# while N != 1:
#     if N % K == 0:
#         N = N / K
#     else:
#         N -= 1
#     answer += 1

while True:
    target = (N // K) * K
    answer += (N - target)
    N = target
    if N < K:
        break
    answer += 1
    N //= K

answer += N - 1
print(answer)