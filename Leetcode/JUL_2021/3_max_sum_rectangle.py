def max_sum_submatrix(matrix, k):
    m, n = len(matrix), len(matrix[0])
    sum_from_start = [[0 for _ in range(m)] for _ in range(n)]

    max_val = -100 * m * n
    def compare_update_val(max_val, val, k):
        if val > max_val and val <= k:
            return val
        return max_val


    for i in range(m):
        j_sum = 0
        for j in range(n):
            j_sum += matrix[i][j]
            if i == 0: sum_from_start[i][j] = j_sum
            else: sum_from_start[i][j] = sum_from_start[i-1][j] + j_sum
            max_val = compare_update_val(max_val, matrix[i][j], k)
            max_val = compare_update_val(max_val, sum_from_start[i][j], k)
            if max_val == k: return max_val
    
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0: continue
            for r_size in range(1, m - i + 1):
                for c_size in range(1, n - j + 1):
                    else:
                        tli, tlj = i, j
                        bri, brj = i + r_size - 1, j + c_size - 1
                        val = sum_from_start[bri][brj] - sum_from_start[tli]




if __name__ == "__main__":
    print(max_sum_submatrix([[2,2,-1]], 3))