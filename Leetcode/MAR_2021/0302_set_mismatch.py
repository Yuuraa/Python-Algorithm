from collections import Counter

def find_error_nums(nums):
    missing_nums = list(set([i + 1 for i in range(n)]) - set(nums))
    assert(len(missing_nums == 1))
    
    missing_num = missing_nums[0]
    count_nums = Counter(nums)
    duplicated_num = -1
    
    for item, count in count_nums.items():
        if count > 1: 
            duplicated_num = item
            break
    
    return [duplicated_num, missing_num]


def find_error_nums_other(nums):
    n = len(nums)
    val_a = -sum(nums) + n*(n+1)//2
    val_b = -sum(num**2 for num in nums) + n * (n+1)*(2*n+1)//6
    return [(val_b-val_a*val_a)//2//val_a, (val_b+val_a*val_a)//2//val_a]