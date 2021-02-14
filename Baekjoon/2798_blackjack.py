from itertools import combinations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
min_diff = m + 1

for combs in combinations(nums, 3):
    val_sum = sum(list(combs))
    if val_sum > m:
        continue
    else:
        if m - val_sum < min_diff:
            min_diff = m - val_sum

print(m - min_diff)