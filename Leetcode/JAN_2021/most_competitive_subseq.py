# Time Exception
def mostCompetitive_bad(nums, k):
    n, left, ans = len(nums), 0, []
    limit = n - k + 1
    
    if k == 1: return [min(nums)]
    if k == n: return nums
    
    while len(ans) < k:
        next_ans = min(nums[left:limit])
        left += nums[left:limit].index(next_ans) + 1
        limit += 1
        ans.append(next_ans)

    return ans


# Other person's solution
def mostCompetitive(nums, k):
    attempts = len(nums) - k
    stack = []
    for num in nums:
        while stack and num < stack[-1] and attempts > 0:
            stack.pop()
            attempts -= 1
        stack.append(num)
    return stack[:k]


if __name__ == "__main__":
    # ans = mostCompetitive([2,4,3,3,5,4,9,6], 4)
    ans = mostCompetitive([3,5,2,6], 2)
    print(ans)