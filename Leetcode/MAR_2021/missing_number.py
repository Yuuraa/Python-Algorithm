# Solution using O(1) extra space and O(n) runtime complexity
def missing_number(nums):
    missing = 0
    for i, num in enumerate(nums):
        missing = missing ^ i ^ num
    missing ^= len(nums)
    return missing


if __name__ == "__main__":
    assert(missing_number([9,6,4,2,3,5,7,0,1]) == 8)
    assert(missing_number([0,1]) == 2)
    assert(missing_number([3,0,1]) == 2)
    assert(missing_number([0]) == 1)
    print("All examples passed")