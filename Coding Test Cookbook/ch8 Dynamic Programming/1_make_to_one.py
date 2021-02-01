x = int(input())
dp = [x + 1 for _ in range(x+1)]


# 나의 풀이.. recursive로 짰다
def make_to_one(num, x):
    if num == 1:
        return 0
    if dp[num] < x + 1:
        return dp[num]
    answer = x + 1
    if num % 5 == 0:
        answer = min(answer, make_to_one(num // 5, x) + 1)
    if num % 3 == 0:
        answer = min(answer, make_to_one(num // 3, x) + 1)
    if num % 2 == 0:
        answer = min(answer, make_to_one(num // 2, x) + 1)
    answer = min(answer, make_to_one(num - 1, x) + 1)
    dp[num] = answer
    return answer

dp_2 = [0 for i in range(x + 1)]
for i in range(2, x + 1):
    dp_2[i] = dp_2[i - 1] + 1
    if i % 2 == 0:
        dp_2[i] = min(dp_2[i], dp_2[i//2] + 1)
    if i % 3 == 0:
        dp_2[i] = min(dp_2[i], dp_2[i//3] + 1)
    if i % 5 == 0:
        dp_2[i] = min(dp_2[i], dp_2[i//5] + 1)


print(make_to_one(x, x))
print(dp_2[x])
