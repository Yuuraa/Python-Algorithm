def kLengthApart(nums, k):
    if k == 0: return True
    dist = k + 1
    for num in nums:
        if num == 1:
            if dist <= k:
                return False
            else:
                dist = 1
        else:
            dist += 1
    return True


if __name__ == "__main__":
    assert(kLengthApart([1,0,0,0,1,0,0,1], 2) == True)
    assert(kLengthApart([1,0,0,1,0,1], 2) == False)
    assert(kLengthApart([1,1,1,1,1], 0) == True)
    assert(kLengthApart([0,1,0,1], 1) == True)