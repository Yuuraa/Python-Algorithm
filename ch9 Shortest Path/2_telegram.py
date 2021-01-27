import heapq

INF = int(1e9) # 무한 설정
# 도시의 수, 도로의 수, 메시지를 보낼 도시 입력
n, m, c = map(int, input().split())

graph = [[] for _ in range(n + 1)]
times = [INF] * (n + 1) # 걸리는 시간을 INF로 초기화

for _ in range(m):
    a, b, time = map(int, input().split())
    graph[a].append((b, time))

def dijkstra(start):
    times[start] = 0
    path = []
    heapq.heappush(path, (start, 0))
    while path:
        node, time = heapq.heappop(path)
        for next_node, next_time in graph[node]:
            if time + next_time > times[next_node]:
                continue
            else:
                times[next_node] = time + next_time
                heapq.heappush(path, (next_node, time + next_time))


dijkstra(c)
count, total_time = 0, 0

for i in range(1, n + 1):
    if times[i] != INF and i != c:
        count += 1
        total_time = max(total_time, times[i])

print(count, total_time)