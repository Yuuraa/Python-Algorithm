def three_sum_multi(arr, target):
    ans = 0
    for i in range(len(arr) - 2):
        for j in range(i+1, len(arr) - 1):
            for k in range(j+1, len(arr)):
                if arr[i] + arr[j] + arr[k] == target:
                    ans += 1

    return ans