def exist(board, word):
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    len_r, len_c = len(board), len(board[0])

    def dfs(r, c, search_id, len_r, len_c):
        print(r, c, ':')
        print(board)
        if search_id >= len(word):
            return True
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr >= 0 and nc >= 0 and nr < len_r and nc < len_c and board[nr][nc] == word[search_id]:
                board[nr][nc] = '0'
                if dfs(nr, nc, search_id + 1, len_r, len_c):
                    return True
                board[nr][nc] = word[search_id]
        return False

    for i in range(len_r):
        for j in range(len_c):
            if board[i][j] == word[0]:
                board[i][j] = '0'
                if dfs(i, j, 1, len_r, len_c):
                    return True
                board[i][j] = word[0]

    return False


# print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(exist([["a","a"]], "aaa"))