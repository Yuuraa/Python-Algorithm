def triangle_number(nums):
    nums.sort()
    count, n = 0, len(nums)

    for i in range(2, n):
        left, right = 0, i - 1
        while left < right:
            if nums[left] + nums[right] > nums[i]:
                count += (right - left)
                right -= 1
            else:
                left += 1

    return count