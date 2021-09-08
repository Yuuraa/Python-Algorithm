n, m = map(int, input().split())
ball_list = list(map(int, input().split()))

ans = 0
for i, ball in enumerate(ball_list):
    for j in range(i+1, len(ball_list)):
        if ball == ball_list[j]:
            continue
        else:
            ans += 1


print(ans)