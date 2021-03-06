import sys
import heapq

n = int(sys.stdin.readline())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

heapq.heapify(nums)

for _ in range(n):
    print(heapq.heappop(nums))