import heapq

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_find(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n = int(input())
parent = [i for i in range(n+1)]
goal_nums = list(map(int, input().split()))
prices = list(map(int, input().split()))
cost_edges = []
costs = [prices]

for i, p in enumerate(prices):
    heapq.heappush(cost_edges, (p, 0, i+1))

for i in range(n):
    creation_cost = list(map(int, input().split()))
    costs.append(creation_cost)
    for j, c in enumerate(creation_cost):
        heapq.heappush(cost_edges, (c, i+1, j+1))

# print(costs)

n_connection, initial_costs = 0, 0
while cost_edges and n_connection < n:
    cost, a, b = heapq.heappop(cost_edges)
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    else:
        union_find(parent, a, b)
        # print(cost, a, b)
        n_connection += 1
        initial_costs += cost

# print(initial_costs)

# 모든 미생물을 일차적으로 생성한 뒤, 각자 최소 생성 비용을 구해야 한다
min_costs = costs[0]
for i in range(n+1):
    for j in range(n):
        min_costs[j] = min(costs[i][j], min_costs[j])
# print(min_costs)
goal_nums = [num - 1 for num in goal_nums]
# print(goal_nums)

additional_costs = sum([num * cost for num, cost in zip(goal_nums, min_costs)])
# print(additional_costs)
print(initial_costs + additional_costs)