import heapq
import sys


heap = []
n_ops = int(sys.stdin.readline())
for _ in range(n_ops):
    op = int(sys.stdin.readline())
    if op == 0:
        if len(heap) > 0: print(-heapq.heappop(heap))
        else: print(0)
    else:
        heapq.heappush(heap, -op)