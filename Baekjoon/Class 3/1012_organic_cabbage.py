from collections import deque

def bfs(r, c, m, n, farm):
    dr = [1, 0, 1, -1]
    dc = [0, 1, 0, -1]

    queue = deque([(r, c)])
    farm[r][c] = 2
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < m and nc < n and nr >= 0 and nc >= 0 and farm[nr][nc] == 1:
                queue.append((nr, nc))
                farm[nr][nc] = 2


def find_neighbored_cabbages(m, n, farm):
    n_warms = 0
    for i in range(m):
        for j in range(n):
            if farm[i][j] == 1:
                n_warms += 1
                bfs(i, j, m, n, farm)
    return n_warms


n_test = int(input())
ans = []

for t in range(n_test):
    n, m, k = map(int, input().split())
    farm = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(k):
        c, r = map(int, input().split())
        farm[r][c] = 1
    ans.append(find_neighbored_cabbages(m, n, farm))


for a in ans:
    print(a)

