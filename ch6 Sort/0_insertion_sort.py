array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def insertion_sort(array):
    for i in range(1, len(array)):
        new_val = array[i]
        for j in range(i, 0, -1):
            if array[j-1] <= new_val:
                break
            else:
                array[j], array[j-1] = array[j-1], array[j]
    return array

if __name__ == "__main__":
    assert (insertion_sort([7, 5, 9, 0, 3, 1, 6, 2, 4, 8]) == ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

