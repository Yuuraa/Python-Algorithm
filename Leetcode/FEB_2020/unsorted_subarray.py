def find_unsorted_subarray(nums):
    diff_nums = [(nums[i-1], nums[i], nums[i] - nums[i-1]) for i in range(1, len(nums))]
    dec_indices = [i for i, (_, _, diff) in enumerate(diff_nums) if diff < 0]

    if not dec_indices: return 0

    sub_start, sub_end = dec_indices[0], dec_indices[-1]
    sub_max = max(diff_nums, key=lambda x: x[0])[0]
    sub_min = min(diff_nums, key=lambda x: x[1])[1]
    print(sub_max, sub_min)
    ans = sub_end - sub_start + 2
    print('left')
    for i in range(sub_start - 1, -1, -1):
        print(nums[i])
        if nums[i] > sub_min:
            ans += 1
        else: break
    print('right')
    for num in nums[sub_end+2:]:
        print(num)
        if num < sub_max:
            ans += 1
        else: break

    print('answer:', ans)


# find_unsorted_subarray([2,6,4,8,10,9,15])
find_unsorted_subarray([3,2,3,2,4])