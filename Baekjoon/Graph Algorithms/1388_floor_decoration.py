n, m = list(map(int, input().split()))
patterns = []

for _ in range(n):
    patterns.append(list(input()))

visited = [[False for _ in range(m)] for _ in range(n)]
tile_graph = []

def search_horizontal(i, j):
    for c in range(j+1, m):
        if patterns[i][c] == "-":
            visited[i][c] = True
        else: break

def search_vertical(i, j):
    p = patterns[i][j]
    for r in range(i+1, n):
        if patterns[r][j] == p:
            visited[r][j] = True
        else: break

num_tiles = 0
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        visited[i][j] = True
        num_tiles += 1
        if patterns[i][j] == "-":
            search_horizontal(i, j)
        else:
            search_vertical(i, j)

print(num_tiles)