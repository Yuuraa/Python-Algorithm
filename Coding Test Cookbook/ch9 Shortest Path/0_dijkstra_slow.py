import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값

# 노드의 갯수, 간선의 갯수 입력받기
n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # a -> b 까지 c의 비용이 듦


def get_smallest_node():
    min_dist = INF
    index = 0 # 가장 최단 거리가 짧은 노드의 인덱스
    for i in range(1, n + 1):
        if distance[i] < min_dist and not visited[i]:
            min_dist = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0 # 시작 노드 까지의 거리는 0
    visited[start] = True # 시작 노드 방문 표시
    for j in graph[start]:
        distance[j[0]] = j[1] # 시작 노드와 연결된 노드들의 거리 값 업데이트
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("Cannot reach")
    else:
        print(distance[i])