import heapq
import sys

input = sys.stdin.readline

def dijkstra(distance, start):
    path = []
    heapq.heappush(path, (start, 0))
    while path:
        curr, cost = heapq.heappop(path)
        for node in graph_dijk[curr]:
            if distance[node] < cost + 1:
                continue
            else:
                distance[node] = cost + 1
                heapq.heappush(path, (node, cost + 1))


def solve_with_dijkstra():
    distance = [INF] * (n + 1) # 모든 노드들까지의 거리를 INF로 초기화
    # 다익스트라 알고리즘으로 start 부터 모든 노드까지의 최단 거리를 정한다.
    distance[1] = 0
    dijkstra(distance, 1) # 1에서 다른 모든 노드까지의 최단 거리를 구한다
    dist_k = distance[k] # 1에서 k까지 가는 최단 거리를 의미한다
    dijkstra(distance, k) # k 에서 다른 모든 노드까지의 최단 거리를 구한다. 이제 distance에는 k로부터의 최단 거리가 담긴다
    if distance[x] == INF or dist_k == INF:
        return(-1)
    else:
        return(dist_k + distance[x])


def solve_with_floyd():
    for i in range(1, n + 1):
        graph_floyd[i][i] = 0 # 자기 자신으로의 거리는 0으로 초기화

    for k in range(1, n + 1):
        for r in range(1, n + 1):
            for c in range(1, n + 1):
                graph_floyd[r][c] = min(graph_floyd[r][c], graph_floyd[r][k] + graph_floyd[k][c])
    
    dist_1k, dist_kx = graph_floyd[1][x], graph_floyd[k][x]
    if dist_1k == INF or dist_kx == INF:
        return -1
    else:
        return dist_1k + dist_kx
    


if __name__ == '__main__':
    input = sys.stdin.readline
    INF = int(1e9)

    # 노드 갯수, 간선 갯수 입력 받기
    n, m = map(int, input().split())
    # 그래프로 각 도시들의 연결을 표현함
    graph_dijk = [set() for _ in range(n + 1)]
    graph_floyd = [[INF] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph_dijk[a].add(b)
        graph_dijk[b].add(a)
        graph_floyd[a][b] = 1
        graph_floyd[b][a] = 1

    x, k = map(int, input().split())

    result = solve_with_dijkstra()
    result2 = solve_with_floyd()

    print(f"Dijkstra result: {result}")
    print(f"Floyd-washall result: {result}")