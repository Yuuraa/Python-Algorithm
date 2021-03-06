import sys
from collections import deque

n = int(input())

queue = deque([])
result = []

def execute_order(queue, result, order):
    order_list = list(order.split())
    if order_list[0] == "push":
        queue.append(int(order_list[1]))
    elif order_list[0] == "pop":
        if queue:
            val = queue.popleft()
            result.append(val)
        else: result.append(-1)
    elif order_list[0] == "size":
        result.append(len(queue))
    elif order_list[0] == "empty":
        result.append(1 if len(queue)==0 else 0)
    elif order_list[0] == "front":
        if not queue: result.append(-1)
        else: result.append(queue[0])
    elif order_list[0] == "back":
        if not queue: result.append(-1)
        else: result.append(queue[-1])
    else:
        print("Invalid order given")


for _ in range(n):
    order = sys.stdin.readline()
    execute_order(queue, result, order)

for r in result:
    print(r)

