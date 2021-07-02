def find_closest_elems_simple(arr, k, x):
    new_arr = [(val, abs(val - x)) for val in arr]
    new_arr.sort(key=lambda x: (x[1], x[0]))
    return sorted([val for val, _ in new_arr[:k]])


def find_closest_elems_pointer(arr, k, x):
    s, e = 0, len(arr) - 1
    while e - s >= k:
        if abs(arr[s] - x) > abs(arr[e] - x):
            s += 1
        else:
            e -= 1
    return arr[s:e+1]


def solution(arr, k, x):
    # return find_closest_elems_simple(arr, k, x)
    return find_closest_elems_pointer(arr, k, x)


if __name__ == "__main__":
    assert (solution(arr = [1,2,3,4,5], k = 4, x = 3) == [1, 2, 3, 4])
    assert (solution(arr = [1,2,3,4,5], k = 4, x = -1
) == [1, 2, 3, 4])
    assert (solution(arr=[1,1,1,10,10,10], k=1, x = 9) == [10])
    print("All test case passed!")