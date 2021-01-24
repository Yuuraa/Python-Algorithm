n, m = map(int, input().split())
MAX_MONEY = 10001

coins = []
money_composition = [MAX_MONEY for _ in range(MAX_MONEY)]
for _ in range(n):
    new_coin = int(input())
    coins.append(new_coin)
    money_composition[new_coin] = 1
coins.sort()

for money in range(m + 1):
    for coin in coins:
        if coin > money:
            break
        if money_composition[money - coin] != MAX_MONEY:
            money_composition[money] = min(money_composition[money - coin] + 1, money_composition[money]) 

answer = -1 if money_composition[m] == MAX_MONEY else money_composition[m]
print(answer)
