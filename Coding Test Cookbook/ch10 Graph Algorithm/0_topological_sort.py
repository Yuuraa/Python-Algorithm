from collections import deque

# 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입 차수 0으로 초기화
indegrees = [0 for _ in range(v + 1)]

graph = [[] for _ in range(v + 1)]

for _ in range(e):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    indegrees[v2] += 1


def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegrees[i] == 0:
            q.append(i)
        
    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        for v2 in graph[now]:
            indegrees[v2] -= 1
            if indegrees[v2] == 0:
                q.append(v2)

    for i in result:
        print(i, end=' ')

topology_sort()

