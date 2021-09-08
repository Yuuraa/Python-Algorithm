r, c = list(map(int, input().split()))

span_dir = [[0, 1], [1, 0]]

pasture = []
for _ in range(r):
    pasture.append(list(input()))

visited = [[False for _ in range(c)] for _ in range(r)]
num_clumps = 0

def find_span(i, j):
    visited[i][j] = True
    for dr, dc in span_dir:
        nr, nc = i + dr, j + dc
        if nr < r and nc < c and pasture[nr][nc] == "#" and not visited[nr][nc]:
            find_span(nr, nc)


for i in range(r):
    for j in range(c):
        if visited[i][j]: continue
        if pasture[i][j] == ".": 
            visited[i][j] = True
            continue
        visited[i][j] = True
        num_clumps += 1
        find_span(i, j)


print(num_clumps)