def coin_change_old(coins, amount):
    if amount == 0: return 0
    if amount < min(coins): return -1
    if amount in coins:
        return 1

    coins.sort(reverse=True)
    for coin in sorted(coins, reverse=True):
        if coin_change(coins, amount - coin) != -1:
            return coin_change(coins, amount - coin) + 1
    
    return -1


from collections import defaultdict
def coin_change(coins, amount):
    coin_dict = defaultdict(int)
    def coin_helper(val):
        if val in coin_dict: return coin_dict[val]
        if val == 0: return 0
        if val < 0: return float("inf")
        coin_dict[val] = min(coin_helper(val - coin) + 1 for coin in coins)
        return coin_dict[val]
    return coin_helper(amount) if coin_helper(amount) != float("inf") else -1



def coin_change_other(coins, amount):
    @lru_cache(None)
    def coin_helper(i):
        if i == 0: return 0
        if i < 0: return float("inf")
        return min(coin_helper(i - coin) + 1 for coin in coins)
    
    return coin_helper(amount) if coin_helper(amount) != float("inf") else -1



print(coin_change([1, 2, 5], 11))
print(coin_change(coins = [2], amount = 3))
print(coin_change(coins = [1], amount = 0))
print(coin_change(coins = [1], amount = 2))
print(coin_change([2,5,10,1], 27)) # 4
print(coin_change([186,419,83,408], 6249)) # 20