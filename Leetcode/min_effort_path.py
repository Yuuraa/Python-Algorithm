def minimumEffortPath(heights):
    m, n = len(heights), len(heights[0])
    neibs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    
    def dfs(LIMIT, x, y):
        visited.add((x, y)) 
        for dx, dy in neibs:
            if 0<=dx+x<m and 0<=dy+y<n and (dx+x, dy+y) not in visited:
                if abs(heights[x][y] - heights[dx+x][dy+y]) <= LIMIT:
                    dfs(LIMIT, dx+x, dy+y)
    
    beg, end = -1, max(max(heights, key=max))
    while beg + 1 < end:
        mid = (beg + end)//2
        visited = set()
        dfs(mid, 0, 0)
        if (m - 1, n - 1) in visited:
            end = mid
        else:
            beg = mid
            
    return end


# 내가 시도한 코드. 시간초과 남
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
min_diff = 1e7

def minimum_effort_path_old(heights):
    m, n, r_len, c_len = 0, 0, len(heights), len(heights[0])
    global min_diff
    visited = [[False for i in range(c_len)] for j in range(r_len)]

    def dfs(r, c, curr_max):
        visited[m][n] = True
        global min_diff
        print(r, c, curr_max, min_diff)
        if curr_max > min_diff:
            return

        if r == r_len -1 and c == c_len -1:
            min_diff = min(curr_max, min_diff)
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr >= 0 and nc >= 0 and nr < r_len and nc < c_len:
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    dfs(nr, nc, max(abs(heights[nr][nc] - heights[r][c]), curr_max))
                    visited[nr][nc] = False

    visited[0][0] = True
    dfs(0, 0, 0)

    return min_diff


# print(minimum_effort_path([[1,2,2],[3,8,2],[5,3,5]]))
# print(minimum_effort_path([[1,2,3],[3,8,4],[5,3,5]]))
# print(minimum_effort_path([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))
print(minimum_effort_path([[1,10,6,7,9,10,4,9]]))