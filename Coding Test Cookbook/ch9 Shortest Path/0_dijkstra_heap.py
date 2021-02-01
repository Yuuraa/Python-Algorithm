import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로를 0으로 설정
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        distance[now] = dist
        for adj_node, d in graph[now]:
            if distance[adj_node] > d + dist:
                distance[adj_node] = d + dist
                heapq.heappush(q, (d + dist, adj_node))

dijkstra(start)

for i in range(1, n +1):
    if distance[i] == INF:
        print("Cannot reach")
    else:
        print(distance[i])
