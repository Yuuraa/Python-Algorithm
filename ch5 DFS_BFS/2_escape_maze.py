from collections import deque

n, m = map(int, input().split())
maze = []
# maze = []
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

for _ in range(n):
    maze.append(list(map(int, input())))


def BFS():
    path = deque([[0,0]])
    maze[0][0] = 1 # Mark visited with cost

    while path:
        r, c = path.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr >= 0 and nc >= 0 and nr < n and nc < m:
                if maze[nr][nc] == 1:
                    maze[nr][nc] = maze[r][c] + 1 # Mark as visited
                    path.append([nr, nc])
    return maze[n-1][m-1]


print(BFS())
    