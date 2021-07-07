def kth_smallest(matrix, k):
    return sorted([matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix))])[k-1]