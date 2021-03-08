import sys
from itertools import combinations
from collections import deque


n = int(input())
populations = [0] + list(map(int, sys.stdin.readline().split()))

nodes = [i for i in range(1, n+1)]
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    adjs = list(map(int, sys.stdin.readline().split()))
    for node in adjs[1:]:
        graph[i].append(node)


def check_connected(combs):
    visited_nodes = [combs[0]]
    print("visited: ")
    queue = deque([combs[0]])
    print(combs)
    # print(queue)

    while queue:
        now = queue.popleft()
        print("Now:" ,now)
        print("Q:" ,queue)
        for adj_node in graph[now]:
            if adj_node in combs and adj_node not in visited_nodes:
                visited_nodes.append(adj_node)
                queue.append(visited_nodes)
    
    return set(visited_nodes) == set(combs)


def population_diff(combs, others):
    sum_combs, sum_others = 0, 0
    for node in combs:
        sum_combs += populations[node]
    for node in others:
        sum_others += populations[node]
    return abs(sum_combs - sum_others)      



def search_through():
    result = sum(populations)
    for num in range(1, n//2):
        for combs in combinations(nodes, num):
            combs = list(combs)
            others = [node for node in nodes if node not in combs]
            if check_connected(combs) and check_connected(others):
                diff = population_diff(combs, others)
                if result > diff:
                    result = diff
    if result == sum(populations):
        return -1
    else:
        return result

print(search_through())


""" Union Find로 풀고자 했던 노력
# graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
# parent = [i for i in range(n+1)]

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, x, y):
#     x = find_parent(parent, x)
#     y = find_parent(parent, y)
#     if x < y:
#         parent[y] = x
#     else:
#         parent[x] = y 


# def find_min_pop(population, graph):
#     pass


# population = [0] + list(map(int, sys.stdin.readline().split()))
# for i in range(n):
#     adj_nodes = (list(map(int, sys.stdin.readline().split())))
#     for adj_node in adj_nodes[1:]:
#         graph[adj_node][i+1] = graph[i+1][adj_node] = 1
#         union_parent(parent, adj_node, i+1)

# print(parent)
# print(population)

# if len(set(parent[1:])) > 2:
#     print(-1)
# elif len(set(parent[1:])) == 2:
#     from collections import defaultdict
#     vals = defaultdict(list)
#     for i, p in enumerate(parent[1:]):
#         vals[p].append(population[i+1])
#     sum_pops = []
#     for pops in vals.values():
#         sum_pops.append(sum(pops))
#     print abs(sum_pops[0] - sum_pops[1])
# else:
#     find_min_pop(population, graph)
"""