INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n+1)]
# 자기 자신에서 자기 자신으로 가는 비용 = 대각선은 0으로 초기화
for i in range(1, n + 1):
    graph[i][i] = 0

# 간선의 입력을 받아 값 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따른 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            graph[r][c] = min(graph[r][c], graph[r][k] + graph[k][c])

# 수행된 결과 출력
for r in range(1, n + 1):
    for c in range(1, n + 1):
        if graph[r][c] == INF:
            print(f"Cannot reach to {c} from {r}", end=" ")
        else:
            print(f"Distance from {r} to {c}: {graph[r][c]}", end=" ")
    print()