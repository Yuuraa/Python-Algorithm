import sys
from collections import deque

n = int(input())
queue = deque([])
result = []

def do_order(order_list):
    order = order_list[0]
    val = int(order_list[1]) if len(order_list) > 1 else None
    
    if order == "push_back":
        queue.append(val)
    elif order == "push_front":
        queue.appendleft(val)
    elif order == "pop_front":
        if queue:
            val = queue.popleft()
            result.append(val)
        else:
            result.append(-1)
    elif order == "pop_back":
        if queue:
            val = queue.pop()
            result.append(val)
        else:
            result.append(-1)
    elif order == "front":
        result.append(queue[0] if queue else -1)
    elif order == "back":
        result.append(queue[-1] if queue else -1)
    elif order == "size":
        result.append(len(queue))
    elif order == "empty":
        result.append(1 if len(queue) == 0 else 0)
    else:
        print("Invalid order")

for _ in range(n):
    order_list = sys.stdin.readline().split()
    do_order(order_list)

for r in result:
    print(r)
