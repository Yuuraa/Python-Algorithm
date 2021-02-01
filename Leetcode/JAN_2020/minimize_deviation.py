import heapq

def minimize_deviation(nums):
    heap = []
    for num in nums:
        tmp = num
        while tmp %2 == 0: tmp //=2
        heap.append((tmp, max(num, tmp*2)))

    max_val = max(i for i, j in heap)
    heapq.heapify(heap)
    ans = float("inf")

    while len(heap) == len(nums):
        num, limit = heapq.heappop(heap)
        ans = min(ans, max_val - num)
        if num < limit:
            heapq.heappush(heap, (num * 2, limit))
            max_val = max(max_val, num * 2)

    return ans

if __name__ == '__main__':
    assert(minimize_deviation([1,2,3,4]) == 1)
    assert(minimize_deviation([4,1,5,20,3]) == 3)
    assert(minimize_deviation([2,10,8]) == 3)
    print("Passed all examples")