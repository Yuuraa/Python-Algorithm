from collections import defaultdict
import math

def num_factored_binary_trees(arr):
    dp = defaultdict(int)
    for num in arr:
        dp[num] += 1
    
    arr.sort()
    for i, num in enumerate(arr):
        for val in arr[:i]:
            if num % val == 0 and num // val in dp:
                # print(f'{num}: {dp[num]}, {val}: {dp[val]}, {num // val}: {dp[num//val]}')
                dp[num] += dp[val] * dp[num//val]
    
    ans = 0
    for num in dp:
        ans += dp[num]
        ans %= (10**9 + 7)

    # print(dp.items())
    # print(ans)
    return ans


def num_factored_binary_trees_sol(arr):
    MOD = 10 ** 9 + 7
    n = len(arr)
    a.sort()
    dp = [1] * n
    index = {x: i for i, x in enumerate(arr)}
    for i, x in enumerate(arr):
        for j in xrange(i):


num_factored_binary_trees(arr = [2,4]) # 3
num_factored_binary_trees(arr = [2,4,5,10]) # 7
num_factored_binary_trees([18,3,6,2]) # 12
num_factored_binary_trees([46,144,5040,4488,544,380,4410,34,11,5,3063808,5550,34496,12,540,28,18,13,2,1056,32710656,31,91872,23,26,240,18720,33,49,4,38,37,1457,3,799,557568,32,1400,47,10,20774,1296,9,21,92928,8704,29,2162,22,1883700,49588,1078,36,44,352,546,19,523370496,476,24,6000,42,30,8,16262400,61600,41,24150,1968,7056,7,35,16,87,20,2730,11616,10912,690,150,25,6,14,1689120,43,3128,27,197472,45,15,585,21645,39,40,2205,17,48,136]) # 509730797