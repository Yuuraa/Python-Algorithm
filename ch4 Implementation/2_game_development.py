m, n = map(int, input().split())
r, c, direction = map(int, input().split())
game_map = []

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i in range(m):
    game_map.append(list(input().split()))

while True:
    for _  in range(4):
        left_dir = ((direction - i - 1) + 4)%4
        nr, nc = r + dr[left_dir], c + dc[left_dir]
        if nr < 0 or nc < 0 or nr >= m or nc >= n:
            continue
        else:
            if game_map[nr][nc] == 0:
                game_map[nr][nc]

