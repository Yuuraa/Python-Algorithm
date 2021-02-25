def find_unsorted_subarray(nums):
    diff_nums = [(nums[i-1], nums[i], nums[i] - nums[i-1]) for i in range(1, len(nums))]
    dec_indices = [i for i, (_, _, diff) in enumerate(diff_nums) if diff < 0]
    dec_pairs = [diff_nums[i] for i in dec_indices]

    # find unsorted pairs in nums array
    if not dec_indices: return 0

    # find initial subarray, starting from first misordered pair to last
    sub_start, sub_end = dec_indices[0], dec_indices[-1]
    # find min value and max value in the subarray
    sub_max = max(dec_pairs, key=lambda x: x[0])[0]
    sub_min = min(dec_pairs, key=lambda x: x[1])[1]

    # if this is the minimum subarray, answer will be same as below
    ans = sub_end - sub_start + 2

    # else, there will be values before the subarray that are larger than the min value of the subarray
    for i in range(sub_start - 1, -1, -1):
        print(nums[i])
        if nums[i] > sub_min:
            ans += 1
        else: break

    # or, there will be values after the subarray that are smaller than the max value of the subarray
    for num in nums[sub_end+2:]:
        print(num)
        if num < sub_max:
            ans += 1
        else: break

    return ans

if __name__ == "__main__":
    assert(find_unsorted_subarray([2,6,4,8,10,9,15]) ==  6)
    assert(find_unsorted_subarray([3,2,3,2,4]) ==  4)
    assert(find_unsorted_subarray([1,2,3,5,4]) ==  2)

    print("All examples passed")