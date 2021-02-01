def quick_sort_old(array, start, end):
    pivot = start # 랜덤하게 고르는 것으로 알고 있는데, 확인 필요
    left, right = start + 1, end

    if end - start <= 0:
        return

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
        else:
            array[pivot], array[right] = array[right], array[pivot]

    quick_sort_old(array, start, right - 1)
    quick_sort_old(array, right + 1, end)


def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    left_array = [num for num in tail if num <= pivot]
    right_array = [num for num in tail if num > pivot]

    return quick_sort(left_array) + [pivot] + quick_sort(right_array)




if __name__ == "__main__":
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    quick_sort_old(array, 0, len(array) - 1)
    assert (array == ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    assert (quick_sort(array) == ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

    print("All examples passed !")

    
    



