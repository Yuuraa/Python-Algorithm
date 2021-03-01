def shoretst_binary_matrix(grid):
    n = len(grid)
    paths = [n** 2 + 1]
    dr = [0, 0, 1, 1, 1, -1, -1, -1]
    dc = [1, -1, 0, 1, -1, 0, 1, -1]
    
    def dfs(r, c, path_len, n):
        if r == n - 1 and c == n - 1:
            paths.append(path_len)
            min_path = min(path_len, min(paths))
        
        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]
            if nr >= 0 and nc >= 0 and nr < n and nc < n and grid[nr][nc] == 0:
                grid[nr][nc] = 2
                dfs(nr, nc, path_len + 1, n)
                grid[nr][nc] = 0                    
    
    dfs(0, 0, 1, n)
    if min(paths) == n ** 2 + 1:
        return -1


def shortestPathBinaryMatrix(self, grid):
    N = len(grid)
    neibs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    queue = deque([(1, 0, 0)]) if grid[0][0] == 0 else deque()
    visited = set()
    
    while queue:
        dist, x, y = queue.popleft()
        if (x, y) == (N-1, N-1): return dist
        for dx, dy in neibs:
            if 0<=x+dx<N and 0<=y+dy<N and grid[x+dx][y+dy] == 0 and (x+dx, y+dy) not in visited:
                visited.add((x+dx,y+dy))
                queue.append((dist + 1, x+dx, y+dy))
            
    return -1