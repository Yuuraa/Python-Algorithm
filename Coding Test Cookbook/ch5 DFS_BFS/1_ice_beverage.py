from collections import deque

n, m = map(int, input().split())

ice_mold, r, c, count = [], 0, 0, 0
visited = [[False for i in range(m)] for j in range(n)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# Get input
for i in range(n):
    ice_mold.append(list(map(int, input())))


# Search with BFS
def BFS(r, c):
    queue = deque([[r,c]])
    visited[r][c] = True
    while queue:
        root_r, root_c = queue.popleft()
        for i in range(4):
            nr, nc = root_r + dr[i], root_c + dc[i]
            if nr >= 0 and nc >= 0 and nr < n and nc < m:
                if not visited[nr][nc] and ice_mold[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append([nr,nc])


# Search with DFS
def DFS(r, c):
    if r < 0 or c < 0 or r >= n or c >= m:
        return
    if visited[r][c]:
        return
    visited[r][c] = True
    if ice_mold[r][c] == 0:
        DFS(r - 1, c)
        DFS(r + 1, c)
        DFS(r, c - 1)
        DFS(r, c + 1)


# Search all possible icecreames
for r in range(n):
    for c in range(m):
        if visited[r][c] or ice_mold[r][c] != 0:
            continue
        else:
            # BFS(r, c)
            DFS(r, c)
            count += 1

print(count)