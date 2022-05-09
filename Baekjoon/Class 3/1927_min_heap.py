import heapq
import sys


heap = []
T = int(sys.stdin.readline())
for _ in range(T):
    op = int(sys.stdin.readline())
    if op == 0:
        if heap: print(heapq.heappop(heap))
        else: print(0)
    else:
        heapq.heappush(heap, op)