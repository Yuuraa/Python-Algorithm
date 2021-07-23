def partition_disjoint(nums):
    left_max = nums[0]
    passed_max = left_max
    left_end = 0
    
    for i in range(1, len(nums)):
        if nums[i] <= left_max:
            left_end = i
            left_max = max(left_max, passed_max)
        else:
            passed_max = max(passed_max, nums[i])

    return left_end + 1


print(partition_disjoint([5, 0, 3, 8, 6]))
print(partition_disjoint([1,1,1,0,6,12]))
    
