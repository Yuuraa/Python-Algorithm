N, M = map(int, input().split())
card_nums = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for r in range(N):
    # min_num = min([card_nums[i][c] for i in range(N)])
    min_num = min(card_nums[r])
    answer = max(min_num, answer)
print(answer)