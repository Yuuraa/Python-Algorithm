m, n = map(int, input().split())
r, c, direction = map(int, input().split())

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

game_map = []
for _ in range(m):
    game_map.append(list(map(int, input().split())))

count, playing = 0, True
while playing:
    progress = False
    for i in range(4):
        left_direction = (direction - i + 3)%4
        nr, nc = r + dr[left_direction], c + dc[left_direction]
        if nr >=0 and nc >= 0 and nr < m and nc < n:
            if game_map[nr][nc] == 0:
                game_map[nr][nc] = 2
                progress = True
                r, c = nr, nc
                direction = left_direction
                break
    if progress:
        count += 1
    else:
        back_direction = (direction + 2)%4
        nr, nc = r + dr[back_direction], c + dc[back_direction]
        if nr >=0 and nc >= 0 and nr < m and nc < n:
            if game_map[nr][nc] == 1:
                playing = False
            else: r, c = nr, nc

print(count)