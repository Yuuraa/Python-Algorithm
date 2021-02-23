def search_matrix(matrix, target):
    for r in matrix:
        if r[0] > target:
            return False
        if r[0] >= target and r[-1] < target:
            if target in r: return True

    return False


def search_matrix2(matrix, target):
    r, c = 0, len(matrix[0]) - 1
    while c >= 0 and r < len(matrix):
        if matrix[r][c] > target:
            c -= 1
        elif matrix[r][c] < targt:
            r += 1
        else:
            return True
    return False