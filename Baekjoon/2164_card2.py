n = int(input())

from collections import deque
nums = deque([i + 1 for i in range(n)])

while len(nums) >= 2:
    nums.popleft()
    second_card = nums.popleft()
    nums.append(second_card)

print(nums[0])