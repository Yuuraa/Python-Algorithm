import sys
import heapq
INF = int(1e9)

n = int(input())
num_microbe = list(map(int, input().split()))
microbe_price = list(map(int, input().split()))
min_incomes = [p for p in microbe_price]

# graph = [[INF for _ in range(n+1)] for _ in range(n+1)] # 초기 상태, 미생물 종류를 노드로 하는 그래프를 그린다. 간선의 가중치는 생성 비용
# graph[0] = [INF] + microbe_price
edges = []
for i in range(n):
    heapq.heappush(edges, (microbe_price[i], 0, i+1))
for i in range(n):
    price = list(map(int, sys.stdin.readline().split()))
    for j, p in enumerate(price):
        min_incomes[j] = min(min_incomes[j], p)
        heapq.heappush(edges, (p, i+1, j+1))


# 다익스트라? 플로이드 워셜 알고리즘을 이용해, 일단 한 차례 모든 미생물을 하나씩 갖게 되기 까지의 최소 비용을 구한다
# # 이후 각 미생물로 들어오는 간선의 가중치의 최솟값을 이용한다. 이 때에는 자기 자신으로의 cycle 값도 포함하기로 한다
# for k in range(n+1):
#     for i in range(n+1):
#         for j in range(n+1):
#             if min_path[i][j] > min_path[i][k] + min_path[k][j]:
#                 min_path[i][j] =  min_path[i][k] + min_path[k][j]


# 구입하는 경우의 비용들을 초기 최솟값으로 둠
# def find_min_microbe(idx):
#     microbe = min_path[idx].index(min(min_path[idx])) # 그 노드에서 갈 수 있는 최솟값을 찾음

# first_microbe = min_path[0].index(min(min_path[0]))
# for r in 

# 모든 미생물 1회 만들 때에는 최소 신장 트리 알고리즘을 사용한다!!
# 이후에는 각 미생물로 들어오는 간선의 가중치의 최솟값을 사용하면 된다
parent = [i for i in range(n+1)]

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

count, initial_price = 0, 0

while edges and count < n+1:
    price, a, b = heapq.heappop(edges)
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    else:
        union_find(parent, a, b)
        count += 1
        initial_price += price

num_microbe = [num - 1 for num in num_microbe]
total_price = initial_price + sum([p*num for p, num in zip(min_incomes, num_microbe)])

print(total_price)
