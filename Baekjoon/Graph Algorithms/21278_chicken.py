from itertools import combinations

n, e = list(map(int, input().split()))

### Part 1. Floid-Washall 알고리즘을 사용해 모든 건물들 사이의 거리를 구함
INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

graph = [[INF] * (n+1) for _ in range(n+1)]
# 자기 자신에서 자기 자신으로 가는 비용 = 대각선은 0으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0

# 간선의 입력을 받아 값 초기화
for _ in range(e):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# 점화식에 따른 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            graph[r][c] = min(graph[r][c], graph[r][k] + graph[k][c])

print(graph)

min_pathsum = INF
store1, store2 = -1, -1

for n1, n2 in combinations(range(1, n+1), 2):
    new_path = []
    for i in range(1, n+1):
        new_path.append(min(graph[n1][i], graph[n2][i]))
    print(n1, n2, new_path)
    if min_pathsum > sum(new_path):
        min_pathsum = sum(new_path)
        store1, store2 = n1, n2

print(store1, store2, min_pathsum*2)


