def max_profit_timelimit(prices, fee):
    def solver(sub_prices, fee, profit):
        # print(sub_prices, profit)
        n = len(sub_prices)
        if n < 2:
            return profit
        ans = 0
        min_i= 5 * (10**4)
        for i in range(n):
            if sub_prices[i] >= min_i:
                continue
            else:
                min_i = sub_prices[i]
            for j in range(i+1, n):
                if sub_prices[j] > sub_prices[i] + fee:
                    val = solver(sub_prices[j+1:], fee, sub_prices[j] - sub_prices[i] - fee)
                    if ans < val:
                        ans =  val
        # print(sub_prices, ans)
        return profit + ans

    return solver(prices, fee, 0)

def max_profit(prices, fee):
    if len(prices) == 1: return 0
    n = len(prices)

    dp, sp = [-float(inf)]*n, [0]*n
    for i in range(n-1):
        dp[i] = prices[i+1] - prices[i] + max(dp[i-1], sp[i-2] - fee)
        sp[i] = max(sp[i-1], dp[i])

    return sp[-2]

print(max_profit(prices = [1,3,2,8,4,9], fee = 2))
print(max_profit(prices = [1,3,7,5,10,3], fee = 3))
print(max_profit([2,1,4,4,2,3,2,5,1,2], 1)) # 4