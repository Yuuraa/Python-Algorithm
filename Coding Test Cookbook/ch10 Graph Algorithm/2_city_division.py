def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

# TODO: heapq를 사용해서 바로 바로 정렬이 되게 해보자
edges = []
result = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))


edges.sort()
last = 0 # 최소 신장 트리에 포함되는 간선 중 가장 비용이 큰 것

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost
    
# 두 개의 분리된 마을을 지을 것이기 때문에, 일단 다 합쳐지게 만든 뒤 하나를 끊어 버리면 된다
print(result - last)

