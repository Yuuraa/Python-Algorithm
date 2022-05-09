import sys
from collections import deque


def explore_farm(farm, i, j, m, n):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    locations = deque()
    locations.append((i, j))
    while locations:
        i, j = locations.popleft()
        farm[i][j] = 2
        for d in range(4):
            ni, nj = i + dx[d], j + dy[d]
            if ni < 0 or nj < 0 or ni >= m or nj >= n: continue
            elif farm[ni][nj] == 1: 
                farm[ni][nj] = 2
                locations.append((ni, nj))


def get_min_cabbage_worms():
    m, n, k = map(int, sys.stdin.readline().split())
    farm = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        farm[x][y] = 1

    worm_cnt = 0
    for i in range(m):
        for j in range(n):
            if farm[i][j] == 1:
                worm_cnt += 1
                explore_farm(farm, i, j, m, n)
    return worm_cnt


T = int(sys.stdin.readline())
for _ in range(T):
    print(get_min_cabbage_worms())