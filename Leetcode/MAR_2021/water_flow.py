from collections import deque


def pacific_atlantic(matrix):
    m, n = len(matrix), len(matrix[0])
    # traveled_ocean = [[0 for _ in range(n)] for _ in range(m)]

    # queue = deque([[0, 0, matrix[0][0]]])
    flowed = [[0 for _ in range(n)] for _ in range(m)]

    def flow_ocean(i, j, matrix, cont_val, change_val):
        di = [1, 0, -1, 0]
        dj = [0, 1, 0, -1]

        if matrix[i][j] == change_val: return
        flowed[i][j] = change_val
        
        queue = deque([(i, j)])
        while queue:
            i, j = queue.popleft()
            curr_flow = matrix[i][j]
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if ni >= 0 and ni < m and nj >= 0 and nj < n and matrix[ni][nj] >= curr_flow and flowed[ni][nj] == cont_val:
                    flowed[ni][nj] = change_val
                    queue.append((ni, nj))
    
    for i in range(m):
        flow_ocean(i, 0, matrix, 0, 1)
    for j in range(n):
        flow_ocean(0, j, matrix, 0, 1)
    for i in range(m):
        flow_ocean(i, n-1, matrix, 1, 2)
    for j in range(n):
        flow_ocean(m-1, j, matrix, 0, 1)


    for i in range(m):
        for 

        


