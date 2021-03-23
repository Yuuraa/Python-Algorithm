from collections import Counter
from itertools import combinations


def three_sum_multi(arr, target):
    count_arr = Counter(arr)
    ans, mod = 0, 10**9 + 7
    
    # Use three duplicate numbers
    if target % 3 == 0 and target // 3 in count_arr and count_arr[target // 3] >= 3:
        n = count_arr[target // 3]
        ans += n*(n-1)*(n-2)// 6 # nC3
        ans %= mod
    

    # Use two duplicate numbers
    for num, count in count_arr.items():
        if count < 2: continue
        remain_val = target - num * 2
        if remain_val != num and remain_val in count_arr:
            ans += count*(count-1)*count_arr[remain_val] // 2
            ans %= mod

    # Use three different numbers
    for num1, num2, num3 in combinations(count_arr.items(), 3):
        if num1[0] + num2[0] + num3[0] == target:
            ans += num1[1] * num2[1] * num3[1]
            ans %= mod

    return ans


if __name__ == "__main__":
    assert(three_sum_multi(arr = [1,1,2,2,2,2], target = 5) == 12)
    assert(three_sum_multi(arr = [1,1,2,2,3,3,4,4,5,5], target = 8) == 20)
    print('All examples passed')