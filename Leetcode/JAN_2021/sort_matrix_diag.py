def diagonal_sort(mat):
    m, n = len(mat), len(mat[0])
    for i in range(m):
        diag_list = [mat[x + i][x] for x in range(min(m-i, n))]
        diag_list.sort()
        for j in range(min(m-i, n)):
            mat[i + j][j] = diag_list[j]

    for j in range(1, n):
        diag_list = sorted([mat[x][x + j] for x in range(min(m, n - j))])
        for i in range(min(m, n - j)):
            mat[i][j + i] = diag_list[i]
    # print(mat)
    return mat


if __name__ == "__main__":
    assert(diagonal_sort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]) == [[1,1,1,1],[1,2,2,2],[1,2,3,3]])
