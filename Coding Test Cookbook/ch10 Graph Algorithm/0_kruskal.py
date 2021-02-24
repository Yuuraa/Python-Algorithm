def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_find(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    

v, e = map(int, input().split())
parent = [i for i in range(v + 1)]
import heapq
edges = []
total_cost, count = 0, 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    # 정렬된 상태로, cost 기준 min_heap에 간선 추가
    heapq.heappush(edges, (cost, a, b))

# Kruskal algorithm - 가중치가 작은 간선들부터 살피며 확인
# 신장 트리라면, v개의 노드에 대해 v - 1개의 간선을 포함해야 하기 때문에 count가 v를 넘어가면 더 이상 확인하지 않음
while edges and count < v :
    # 가장 작은 cost를 가진 간선부터 확인
    cost, a, b = heapq.heappop(edges)
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    else:
        union_find(parent, a, b)
        total_cost += cost

print(total_cost)


# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25

# 답: 159