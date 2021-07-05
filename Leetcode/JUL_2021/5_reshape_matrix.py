def matrix_reshape(mat, r, c):
    old_r, old_c = len(mat), len(mat[0])
    if r*c != old_r * old_c: return mat

    new_mat = [[] for _ in range(r)]
    for i in range(r*c):
        new_mat[i//c].append(mat[i//old_c][i%old_c])
    
    return new_mat


if __name__ == "__main__":
    assert(matrix_reshape([[1, 2], [3, 4]], 1, 4) == [[1, 2, 3, 4]])
    assert(matrix_reshape([[1, 2], [3, 4]], 2, 4) == [[1, 2], [3, 4]])
    print("All test cases passed")