def maximal_square(matrix):
    def square_size(i, j, max_size):
        for size in range(1, max_size + 1):
            for di in range(size):
                if matrix[i+di][j+size-1] == '0':
                    return size - 1
            for dj in range(size):
                if matrix[i+size-1][j+dj] == '0':
                    return size - 1
        return max_size
    
    ans = 0
    m, n = len(matrix), len(matrix[0])

    for i in range(m):
        for j in range(n):
            max_size = min(m - i, n - j)
            possible_size = square_size(i, j, max_size)
            if ans < possible_size: ans = possible_size
    
    return ans**2


if __name__ == "__main__":
    assert(maximal_square([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) == 4)
    assert(maximal_square([["0","1"],["1","0"]]) == 1)
    assert(maximal_square([["0"]]) == 0)
    print("All examples passed")