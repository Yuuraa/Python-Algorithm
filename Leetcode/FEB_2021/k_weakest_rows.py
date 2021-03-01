def k_weakest_rows(mat, k):
    indexed_rows = sorted([(i, row.count(0)) for i, row in enumerate(mat)], key=lambda x:(-x[1], x[0]))
    return [idx for idx, _ in indexed_rows[:k]]


if __name__ == "__main__":
    assert k_weakest_rows(mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2) == [0,2]
    assert k_weakest_rows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 3) == [2,0,3]
    print("Test cases passed!")