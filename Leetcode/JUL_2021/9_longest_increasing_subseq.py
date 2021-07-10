def length_of_lis(nums):
    dp = [1 for _ in range(len(nums))]
    for i in range(len(nums)):
        for j in range(i-1, -1, -1):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)


if __name__ == "__main__":
    print(length_of_lis([10,9,2,5,3,7,101,18]))
    print(length_of_lis([0,1,0,3,2,3]))
    print(length_of_lis([7,7,7,7,7,7]))