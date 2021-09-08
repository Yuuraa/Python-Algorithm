n, m = list(map(int, input().split()))

map = []
for _ in range(n):
    map.append(str(input()))

def count_seashore(i, j):
    if map[i][j] == ".": return 0
    row_diff = -1 if i % 2 == 0 else 1
    move_r = [1, -1, 1, -1, 0, 0]
    move_c = [row_diff, row_diff, 0, 0, 1, -1]
    count = 0
    for dr, dc in zip(move_r, move_c):
        ni, nj = i + dr, j + dc
        if ni >= 0 and nj >= 0 and ni < n and nj < m:
            if map[ni][nj] == ".":
                count += 1
    return count


ans = 0
for i in range(n):
    for j in range(m):
        if map[i][j] == "#":
            cnt = count_seashore(i, j)
            ans += cnt


print(ans)