# Beautiful array: No k with i < k < j such that nums[i] + nums[j] = nums[k]

def check_and_add(nums, val):
    for k in range(len(nums) + 1):
        is_ok = True
        i  = 0
        while is_ok and i < k:
            for j in range(k, len(nums)):
                if nums[i] + nums[j] == val *2:
                    is_ok = False
                    break
            i += 1

        i = 0
        while is_ok and i < k-2:
            for j in range(i+1, k-1):
                if nums[i] == nums[j]*2 - val:
                    is_ok = False
                    break
            i += 1

        i = k
        while is_ok and i < len(nums)-1:
            for j in range (i+1, len(nums)):
                if nums[i]*2 == nums[j] + val:
                    is_ok = False
                    break
            i += 1
            
        if is_ok:
            return nums[:k] + [val] + nums[k:]

    return nums





def beautiful_array(n):
    # added = [False for _ in range(n+1)]
    nums = [n]
    for val in range(1, n):
        nums = check_and_add(nums, val)
    return nums

print(beautiful_array(4))
print(beautiful_array(5))
print(beautiful_array(1)) # [1]
print(len(beautiful_array(100)))


