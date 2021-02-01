def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 1:
        return
    
    # 바꿔치기 될 기준을 찾음
    # 기준 이후에서 자신보다 큰 값들 중 최솟값을 찾아냄
    swap_id, swap_val = -1, -1
    for i in range(len(nums) - 1):
        if nums[i + 1] > nums[i]:
            swap_id = i
            swap_val = nums[i]
    
    if swap_val < 0:
        nums[:] = nums[::-1]
        return

    min_val, min_id = nums[swap_id + 1], swap_id + 1
    for i in range(swap_id+1, len(nums)):
        if nums[i] > swap_val:
            if nums[i] <= min_val:
                min_val = nums[i]
                min_id = i

    nums[swap_id] = min_val
    nums[min_id] = swap_val

    nums[swap_id+1:] = nums[swap_id+1:][::-1]

def nextPermutation_other(nums):
    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start, end = start + 1, end - 1
        
    i, n = len(nums) - 1, len(nums)
    while i >= 1 and nums[i] <= nums[i-1]:
        i -= 1
    
    if i != 0:
        j = i
        while j + 1 < n and nums[j + 1] > nums[j - 1]:
            j += 1
        nums[i-1], nums[j] = nums[j], nums[i-1]
    
    reverse(nums, i , n - 1)


if __name__ == "__main__":
    arr1 = [2, 3, 1, 3, 3]
    nextPermutation(arr1)
    arr2 = [3, 2, 1]
    nextPermutation(arr2)
    arr3 = [1, 2, 3]
    nextPermutation(arr3)
    
    assert(arr1 == [2, 3, 3, 1, 3])
    assert(arr2 == [1, 2, 3])
    assert(arr3 == [1, 3, 2])
    print("All samples passed")
