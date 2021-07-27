import heapq


def three_sum_closest(nums, target):
    nums.sort()
    diffs = []
    n = len(nums)
    for i in range(n-2):
        l, r = i+1, n-1
        temp_target = target - nums[i]
        while l < r:
            sum_val = nums[l] + nums[r]
            if sum_val == temp_target:
                return target
            elif sum_val < temp_target:
                l += 1
                heapq.heappush(diffs, (temp_target - sum_val, sum_val + nums[i]))
            else:
                r -= 1
                heapq.heappush(diffs, (sum_val - temp_target, sum_val + nums[i]))
    return diffs[0][1]

