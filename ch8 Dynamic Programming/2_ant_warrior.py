n = int(input())
food_list = list(map(int, input().split()))

# 바로 전의 식량 창고에서 훔친 경우가 max_foods[0],
# 직전의 식량 창고에서 훔치지 않은 경우가 max_foods[1] 이다
# === 나의 풀이 (공간과 연산이 두 배임) ===
'''
max_foods = [[0 for _ in range(2)] for _ in range(n)]
max_foods[0][0], max_foods[0][1], max_foods[1][0], max_foods[1][1] = food_list[0], food_list[0], food_list[0], food_list[1]

for i in range(2, n):
    max_foods[i][0] = max(max_foods[i-1][0], max_foods[i-1][1])
    max_foods[i][1] = max(max_foods[i-2][0], max_foods[i-2][1]) + food_list[i]

print(max(max_foods[n-1][0], max_foods[n-1][1]))
'''

# === 책에서의 풀이 ===
max_foods = [0 for _ in range(n)]
max_foods[0], max_foods[1] = food_list[0], food_list[1]
for i in range(2, n):
    max_foods[i] = max(max_foods[i-1], max_foods[i-2] + food_list[i])
print(max_foods[n-1])