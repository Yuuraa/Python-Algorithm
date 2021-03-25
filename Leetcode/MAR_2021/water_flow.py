from collections import deque


def pacific_atlantic(matrix):
    if not matrix: return []
    m, n = len(matrix), len(matrix[0])
    flowed = [[0 for _ in range(n)] for _ in range(m)]

    def flow_ocean(i, j, matrix):
        di = [1, 0, -1, 0]
        dj = [0, 1, 0, -1]
        
        if not visited[i][j]:
            queue = deque([(i, j)])
            flowed[i][j] += 1
            visited[i][j] = True
        else: return
        
        while queue:
            i, j = queue.popleft()
            curr_flow = matrix[i][j]
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if ni >= 0 and ni < m and nj >= 0 and nj < n and matrix[ni][nj] >= curr_flow and not visited[ni][nj]:
                    flowed[ni][nj] += 1
                    visited[ni][nj] = True
                    queue.append((ni, nj))
    
    visited = [[False for _ in range(n)] for _ in range(m)]
    for i in range(m):
        flow_ocean(i, 0, matrix)
    for j in range(n):
        flow_ocean(0, j, matrix)
    
    visited = [[False for _ in range(n)] for _ in range(m)]
    for i in range(m):
        flow_ocean(i, n-1, matrix)
    for j in range(n):
        flow_ocean(m-1, j, matrix)


    ans = []
    for i in range(m):
        for j in range(n):
            if flowed[i][j] == 2:
                ans.append([i, j])

    return ans


if __name__ == "__main__":
    assert(pacific_atlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]) == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]])
    assert(pacific_atlantic([]) == [])    

    print("All examples passed")
