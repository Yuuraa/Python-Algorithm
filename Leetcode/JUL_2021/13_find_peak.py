def is_peak(nums, mid):
    if mid > 0 and mid < len(nums) - 1:
        return nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]
    elif mid == 0:
        return nums[mid] > nums[mid+1]
    elif mid == len(nums) - 1:
        return nums[mid] > nums[mid-1]


def find_peak_element(nums):
    if len(nums) == 1: return 0
    if len(nums) == 2:
        return 0 if nums[0] > nums[1] else 1

    s, e = 0, len(nums) - 1
    while s <= e:
        mid = (s + e) // 2
        if is_peak(nums, mid):
            return mid
        else:
            if nums[mid+1] > nums[mid]:
                s = mid + 1
            else:
                e = mid - 1
    return s


print(find_peak_element([1,2,3,1]))
print(find_peak_element([1,2,1,3,5,6,4]))
