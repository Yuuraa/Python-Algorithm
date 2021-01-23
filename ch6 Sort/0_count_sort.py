def count_sort(array, left_limit, right_limit):
    count_list = [0 for _ in range(left_limit, right_limit + 1)]
    sorted_array = []

    for num in array:
        count_list[num - left_limit] += 1
    
    for i, count in enumerate(count_list):
        sorted_array.extend([left_limit + i] * count)

    return sorted_array


if __name__ == "__main__":
    assert (count_sort([7, 5, 9, 0, 3, 1, 6, 2, 4, 8], 0, 9) == ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print("All examples passed!")