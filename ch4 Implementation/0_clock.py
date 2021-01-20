n = int(input())
answer = 0

# 경우의 수가 86,400가지이므로 즉, 100,000개도 되지 않으므로
# 단순히 시각을 증가시키며 확인해도 된다
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                answer += 1

print(answer)