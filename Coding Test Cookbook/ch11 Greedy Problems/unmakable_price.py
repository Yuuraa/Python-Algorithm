n = int(input())

coins = list(map(int, input().split()))
coins.sort()

target = 1
for x in coins:
    if x > target:
        break
    else:
        target += x

print(target)